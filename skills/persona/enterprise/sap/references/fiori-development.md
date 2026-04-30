# SAP Fiori Development Guide

> Comprehensive guide for building SAP Fiori applications.

---

## 1. Fiori Overview

### 1.1 Design Philosophy

SAP Fiori is the design language and UX paradigm for SAP applications, providing:
- Role-based, consumer-grade user experience
- Consistent design across all SAP applications
- Responsive design for all devices
- Simple, intuitive interactions

### 1.2 Fiori Design Principles

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FIORI DESIGN PRINCIPLES                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   ROLE-     │  │   ADAPTIVE  │  │   COHERENT  │  │   SIMPLE    │    │
│  │   BASED     │  │             │  │             │  │             │    │
│  │             │  │             │  │             │  │             │    │
│  │ Tailored to │  │ Works on    │  │ Consistent  │  │ Focus on    │    │
│  │ specific    │  │ desktop,    │  │ across all  │  │ essential   │    │
│  │ user roles  │  │ tablet,     │  │ SAP apps    │  │ tasks       │    │
│  │ and tasks   │  │ mobile      │  │             │  │             │    │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │
│                                                                         │
│  ┌─────────────┐  ┌─────────────┐                                       │
│  │   DELIGHTFUL│  │   FAST      │                                       │
│  │             │  │             │                                       │
│  │ Consumer-   │  │ Real-time   │                                       │
│  │ grade UX    │  │ data, fast  │                                       │
│  │             │  │ response    │                                       │
│  └─────────────┘  └─────────────┘                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Fiori Architecture

### 2.1 Technology Stack

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FIORI TECHNOLOGY STACK                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PRESENTATION LAYER                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  SAP Fiori Elements    │   Freestyle SAPUI5                    │   │
│  │  • List Report         │   • Custom views                      │   │
│  │  • Object Page         │   • Custom controllers                │   │
│  │  • Overview Page       │   • Custom controls                   │   │
│  │  • Worklist            │                                       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  FRAMEWORK LAYER                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  SAPUI5 Framework                                                  │   │
│  │  • MVC architecture    • Data binding    • Routing               │   │
│  │  • OData model         • i18n            • Component              │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  DATA LAYER                                                             │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  OData Services / REST APIs / CDS Views                            │   │
│  │  • S/4HANA OData       • CAP Services    • Custom APIs           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  PLATFORM LAYER                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  SAP BTP / S/4HANA / SAP Build Work Zone                           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Fiori Elements vs Freestyle

| Aspect | Fiori Elements | Freestyle |
|--------|----------------|-----------|
| **Development Speed** | Fast (annotation-driven) | Slower (custom coding) |
| **Flexibility** | Limited to templates | Unlimited |
| **Maintenance** | Lower (upgrade-stable) | Higher |
| **Best For** | Standard CRUD apps | Complex custom UIs |
| **Learning Curve** | Lower | Higher |

---

## 3. Fiori Elements Development

### 3.1 List Report Page

**CDS Annotations for List Report:**
```cds
@UI: {
  headerInfo: {
    typeName: 'Purchase Order',
    typeNamePlural: 'Purchase Orders'
  },
  selectionPresentationVariant: [{
    qualifier: 'Default',
    presentationVariant: {
      sortOrder: [{ by: 'PO_Number', direction: #DESC }],
      visualizations: [{
        type: #AS_LINE_ITEM,
        valueQualifier: 'Default'
      }]
    }
  }]
}
entity PurchaseOrder {
  @UI.lineItem: [{ position: 10, importance: #HIGH }]
  key PO_Number : String(10);
  
  @UI.lineItem: [{ position: 20, importance: #HIGH }]
  Vendor_Name : String(100);
  
  @UI.lineItem: [{ position: 30, importance: #MEDIUM }]
  @Semantics.amount.currencyCode: 'Currency'
  Total_Amount : Decimal(15, 2);
  
  @UI.lineItem: [{ position: 40, importance: #MEDIUM }]
  Currency : Currency;
  
  @UI.lineItem: [{ 
    position: 50, 
    importance: #HIGH,
    criticality: 'Status_Criticality'
  }]
  Status : String(20);
};
```

### 3.2 Object Page

**Object Page Structure:**
```
┌─────────────────────────────────────────────────────────────────────────┐
│  HEADER                                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Title │ Subtitle │ Status │ Actions                            │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  HEADER FACETS (Key information)                                        │
│  ┌──────────┬──────────┬──────────┬──────────┐                        │
│  │ Vendor   │ Amount   │ Date     │ Priority │                        │
│  └──────────┴──────────┴──────────┴──────────┘                        │
│                                                                         │
│  SECTIONS                                                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ General Information                                             │   │
│  │ ┌─────────────────────────────────────────────────────────────┐ │   │
│  │ │ Form: Details, References                                   │ │   │
│  │ └─────────────────────────────────────────────────────────────┘ │   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │ Line Items                                                      │   │
│  │ ┌─────────────────────────────────────────────────────────────┐ │   │
│  │ │ Table: Products, Quantities, Prices                         │ │   │
│  │ └─────────────────────────────────────────────────────────────┘ │   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │ Notes & Attachments                                             │   │
│  │ ┌─────────────────────────────────────────────────────────────┐ │   │
│  │ │ Text area, File upload                                      │ │   │
│  │ └─────────────────────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. SAPUI5 Development

### 4.1 MVC Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MVC ARCHITECTURE                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│     VIEW (XML)              CONTROLLER (JS)           MODEL (JSON/OData)│
│  ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐ │
│  │ <mvc:View>      │◄────►│ onInit()        │◄────►│ oDataModel      │ │
│  │   <Table        │      │ onBeforeRendering│     │   /PurchaseOrder│ │
│  │     items="{     │      │ onAfterRendering │     │                 │ │
│  │       path:      │      │                 │      │ Two-way binding │ │
│  │       '/POs'     │      │ onPress()       │      │                 │ │
│  │     }"           │      │ onSearch()      │      │                 │ │
│  │   >              │      │ formatters      │      │                 │ │
│  │ </mvc:View>      │      │                 │      │                 │ │
│  └─────────────────┘      └─────────────────┘      └─────────────────┘ │
│                                                                         │
│  Responsibilities:                                                      │
│  • View: UI structure, binding expressions                              │
│  • Controller: Event handling, business logic                           │
│  • Model: Data access, validation                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Component Structure

```
webapp/
├── Component.js              # Application component
├── manifest.json             # App descriptor
├── i18n/
│   └── i18n.properties       # Translations
├── controller/
│   ├── App.controller.js
│   └── Main.controller.js
├── view/
│   ├── App.view.xml
│   └── Main.view.xml
├── model/
│   ├── models.js
│   └── formatter.js
├── css/
│   └── style.css
└── localService/
    └── metadata.xml          # OData metadata
```

### 4.3 Key Coding Patterns

**Data Binding:**
```javascript
// One-way binding (read-only)
<Text text="{ProductName}" />

// Two-way binding (editable)
<Input value="{ProductName}" />

// Formatting
<Text text="{
  path: 'Price',
  type: 'sap.ui.model.type.Currency',
  formatOptions: {
    currencyCode: '{Currency}',
    showMeasure: false
  }
}" />

// Expression binding
<ObjectStatus 
  text="{Status}"
  state="{
    path: 'Status',
    formatter: '.formatter.statusState'
  }" />
```

**Event Handling:**
```javascript
// Controller method
onItemPress: function(oEvent) {
  var oItem = oEvent.getSource();
  var oContext = oItem.getBindingContext();
  var sPath = oContext.getPath();
  
  this.getRouter().navTo("detail", {
    POId: oContext.getProperty("PO_Number")
  });
}
```

---

## 5. Fiori Launchpad Configuration

### 5.1 Launchpad Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│  SAP FIORI LAUNCHPAD                                                    │
├─────────────────────────────────────────────────────────────────────────┤
│  [Logo]  Search...            [Apps] [Notifications] [User]            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  MY HOME                                                        │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │   │
│  │  │App Tile 1│ │App Tile 2│ │App Tile 3│ │App Tile 4│          │   │
│  │  │          │ │          │ │          │ │          │          │   │
│  │  │  [icon]  │ │  [icon]  │ │  [icon]  │ │  [icon]  │          │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  PURCHASING GROUP                                               │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐                        │   │
│  │  │ Purchase │ │ Vendor   │ │ Contracts│                        │   │
│  │  │ Orders   │ │ Master   │ │          │                        │   │
│  │  └──────────┘ └──────────┘ └──────────┘                        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  ANALYTICS                                                      │   │
│  │  ┌──────────┐ ┌──────────┐                                      │   │
│  │  │ Spend    │ │ Supplier │                                      │   │
│  │  │ Analysis │ │ Performance                                  │   │
│  │  └──────────┘ └──────────┘                                      │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 App Descriptor (manifest.json)

```json
{
  "_version": "1.12.0",
  "sap.app": {
    "id": "com.myorg.purchaseorders",
    "type": "application",
    "i18n": "i18n/i18n.properties",
    "title": "{{appTitle}}",
    "description": "{{appDescription}}",
    "applicationVersion": {
      "version": "1.0.0"
    },
    "dataSources": {
      "mainService": {
        "uri": "/sap/opu/odata/sap/ZPURCHASE_ORDER_SRV/",
        "type": "OData",
        "settings": {
          "odataVersion": "2.0"
        }
      }
    }
  },
  "sap.ui": {
    "technology": "UI5",
    "deviceTypes": {
      "desktop": true,
      "tablet": true,
      "phone": false
    }
  },
  "sap.ui5": {
    "dependencies": {
      "minUI5Version": "1.120.0",
      "libs": {
        "sap.ui.core": {},
        "sap.m": {},
        "sap.f": {}
      }
    },
    "models": {
      "i18n": {
        "type": "sap.ui.model.resource.ResourceModel",
        "settings": {
          "bundleName": "com.myorg.purchaseorders.i18n.i18n"
        }
      },
      "": {
        "dataSource": "mainService",
        "preload": true,
        "settings": {
          "defaultBindingMode": "TwoWay"
        }
      }
    },
    "routing": {
      "config": {
        "routerClass": "sap.f.routing.Router",
        "viewType": "XML",
        "path": "com.myorg.purchaseorders.view",
        "controlId": "layout",
        "controlAggregation": "beginColumnPages"
      },
      "routes": [
        {
          "pattern": "",
          "name": "list",
          "target": "list"
        },
        {
          "pattern": "PO/{POId}",
          "name": "detail",
          "target": ["list", "detail"]
        }
      ]
    }
  },
  "sap.fiori": {
    "registrationIds": ["F2016"],
    "archeType": "transactional"
  }
}
```

---

## 6. Best Practices

### 6.1 Performance Guidelines

| Guideline | Implementation |
|-----------|----------------|
| **Lazy Loading** | Load data only when needed |
| **OData $expand** | Fetch related data in single call |
| **Pagination** | Use $top/$skip for large lists |
| **Debouncing** | Delay search until typing stops |
| **Busy Indicators** | Show loading state for long operations |

### 6.2 Accessibility

```xmln
<!-- Accessible table -->
<Table 
  ariaLabelledBy="tableTitle"
  growing="true"
  growingScrollToLoad="true">
  <columns>
    <Column 
      minScreenWidth="Tablet"
      demandPopin="true"
      hAlign="Begin">
      <Text text="{i18n>columnProductName}" />
    </Column>
  </columns>
</Table>

<!-- Accessible button -->
<Button 
  text="{i18n>buttonSubmit}"
  tooltip="{i18n>buttonSubmitTooltip}"
  ariaLabelledBy="submitLabel"
  press=".onSubmitPress" />
```

---

*For the latest Fiori guidelines, visit: https://experience.sap.com/fiori-design-web/*

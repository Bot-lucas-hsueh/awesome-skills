# Document Cloud API Reference

## Overview

Adobe Document Cloud provides APIs for PDF manipulation, electronic signatures, and document intelligence. Services are available through Acrobat Services API (formerly PDF Services API) and Acrobat Sign API.

## Acrobat Services API

### Authentication

```javascript
// OAuth 2.0 Client Credentials Flow
const getAccessToken = async () => {
  const response = await fetch('https://pdf-services.adobe.io/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
      'grant_type': 'client_credentials'
    })
  });
  
  const { access_token } = await response.json();
  return access_token;
};
```

### Core Operations

#### PDF Creation

**Create PDF from Office**:
```javascript
const createPDF = async (sourceDocument) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/createpdf', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: sourceDocument.assetId,
      outputFormat: 'pdf'
    })
  });
  
  return response.json();
};
```

**Document Generation**:
```javascript
const generateDocument = async (template, data) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/documentgeneration', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: template.assetId,
      outputFormat: 'pdf',
      jsonDataForMerge: data,
      fragments: {
        // Complex tables and nested structures
        tableRepeatingRows: true,
        horizontalTableRepeat: true,
        nestedTables: true
      }
    })
  });
  
  return response.json();
};

// Usage
const invoiceData = {
  "customerName": "Acme Corporation",
  "invoiceNumber": "INV-2024-001",
  "invoiceDate": "2024-03-21",
  "lineItems": [
    { "description": "Product A", "quantity": 2, "price": 100.00 },
    { "description": "Product B", "quantity": 1, "price": 250.00 }
  ],
  "subtotal": 450.00,
  "tax": 36.00,
  "total": 486.00
};
```

#### PDF Manipulation

**Extract Text and Tables**:
```javascript
const extractPDF = async (document) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/extractpdf', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: document.assetId,
      elementsToExtract: [
        'text',
        'tables',
        'paragraphStyles',
        'boundingBoxes'
      ],
      tableOutputFormat: 'csv'
    })
  });
  
  return response.json();
};

// Response Structure
{
  "elements": [
    {
      "Bounds": [x1, y1, x2, y2],
      "Font": { "family": "Arial", "size": 12 },
      "Page": 1,
      "Path": "//Document/Section/Paragraph[1]",
      "Text": "Extracted text content"
    }
  ],
  "tables": [
    {
      "headers": ["Column 1", "Column 2"],
      "rows": [
        ["Data 1", "Data 2"],
        ["Data 3", "Data 4"]
      ]
    }
  ]
}
```

**Combine PDFs**:
```javascript
const combinePDFs = async (documents) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/combinepdf', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assets: documents.map(doc => ({
        assetID: doc.assetId,
        pageRanges: doc.pageRanges || []
      }))
    })
  });
  
  return response.json();
};
```

**OCR (Optical Character Recognition)**:
```javascript
const ocrPDF = async (document) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/ocr', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: document.assetId,
      ocrType: 'SEARCHABLE_IMAGE', // or 'SEARCHABLE_IMAGE_EXACT'
      locale: 'en-US'
    })
  });
  
  return response.json();
};
```

#### PDF Protection

**Add Password**:
```javascript
const protectPDF = async (document) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/protectpdf', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: document.assetId,
      passwordProtection: {
        userPassword: 'open-password',
        ownerPassword: 'permissions-password',
        encryptionAlgorithm: 'AES_256',
        permissions: {
          printingAllowed: 'HIGH_QUALITY',
          editingAllowed: false,
          copyAllowed: false
        }
      }
    })
  });
  
  return response.json();
};
```

**Remove Password**:
```javascript
const removeProtection = async (document, password) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/removeprotection', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: document.assetId,
      password: password
    })
  });
  
  return response.json();
};
```

#### PDF Properties

**Get PDF Properties**:
```javascript
const getProperties = async (document) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/pdfproperties', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: document.assetId
    })
  });
  
  return response.json();
};

// Response
{
  "document": {
    "name": "document.pdf",
    "pageCount": 10,
    "fileSize": 245760,
    "linearized": false,
    "version": "1.7",
    "encrypted": true
  },
  "pages": [
    {
      "pageNumber": 1,
      "width": 612,
      "height": 792,
      "rotation": 0
    }
  ],
  "fonts": [
    {
      "family": "Helvetica",
      "type": "Type1",
      "embedded": true
    }
  ],
  "forms": {
    "hasXfa": false,
    "hasAcroform": true,
    "fields": 15
  }
}
```

### PDF Embed API

**Basic Integration**:
```html
<!DOCTYPE html>
<html>
<head>
  <title>PDF Embed Example</title>
  <script src="https://documentcloud.adobe.com/view-sdk/main.js"></script>
</head>
<body>
  <div id="adobe-dc-view" style="width: 100%; height: 600px;"></div>
  
  <script type="text/javascript">
    document.addEventListener("adobe_dc_view_sdk.ready", function() {
      const adobeDCView = new AdobeDC.View({
        clientId: "YOUR_CLIENT_ID",
        divId: "adobe-dc-view"
      });
      
      adobeDCView.previewFile({
        content: { location: { url: "https://example.com/document.pdf" } },
        metaData: { fileName: "document.pdf" }
      }, {
        embedMode: "FULL_WINDOW",
        showDownloadPDF: true,
        showPrintPDF: true,
        showLeftHandPanel: true,
        showAnnotationTools: true
      });
    });
  </script>
</body>
</html>
```

**Event Handling**:
```javascript
const eventOptions = {
  // Listen for annotation events
  enableAnnotationEvents: true
};

adobeDCView.registerCallback(
  AdobeDC.View.Enum.CallbackType.EVENT_LISTENER,
  function(event) {
    console.log("Event type:", event.type);
    console.log("Event data:", event.data);
    
    switch(event.type) {
      case "ANNOTATION_ADDED":
        saveAnnotation(event.data);
        break;
      case "ANNOTATION_UPDATED":
        updateAnnotation(event.data);
        break;
      case "ANNOTATION_DELETED":
        deleteAnnotation(event.data);
        break;
      case "DOCUMENT_DOWNLOAD":
        logDownload(event.data);
        break;
    }
  },
  eventOptions
);
```

### PDF Accessibility

**Auto-Tag API**:
```javascript
const autoTagPDF = async (document) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/autotag', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: document.assetId,
      generateReport: true, // Accessibility report
      shiftHeadings: false  // Adjust heading levels
    })
  });
  
  return response.json();
};
```

**Accessibility Checker**:
```javascript
const checkAccessibility = async (document) => {
  const response = await fetch('https://pdf-services.adobe.io/operation/accessibilitychecker', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
      'x-api-key': CLIENT_ID
    },
    body: JSON.stringify({
      assetID: document.assetId,
      reportFormat: 'json' // or 'html'
    })
  });
  
  return response.json();
};
```

## Acrobat Sign API

### Authentication

```javascript
// OAuth 2.0 with Authorization Code Flow
const getSignAccessToken = async (authCode) => {
  const response = await fetch('https://api.adobesign.com/oauth/v2/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      'grant_type': 'authorization_code',
      'client_id': SIGN_CLIENT_ID,
      'client_secret': SIGN_CLIENT_SECRET,
      'code': authCode,
      'redirect_uri': REDIRECT_URI
    })
  });
  
  return response.json();
};
```

### Agreement Management

**Send Agreement**:
```javascript
const sendAgreement = async (document, recipients) => {
  const response = await fetch('https://api.adobesign.com/api/rest/v6/agreements', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${signAccessToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: "Service Agreement",
      fileInfos: [{
        transientDocumentId: document.transientId
      }],
      participantSetsInfo: recipients.map((recipient, index) => ({
        memberInfos: [{
          email: recipient.email,
          firstName: recipient.firstName,
          lastName: recipient.lastName
        }],
        order: index + 1,
        role: recipient.role // SIGNER, APPROVER, DELEGATE
      })),
      signatureType: "ESIGN", // or "WRITTEN"
      state: "IN_PROCESS"
    })
  });
  
  return response.json();
};
```

**Create Transient Document**:
```javascript
const uploadDocument = async (file) => {
  const formData = new FormData();
  formData.append('File', file);
  
  const response = await fetch('https://api.adobesign.com/api/rest/v6/transientDocuments', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${signAccessToken}`
    },
    body: formData
  });
  
  return response.json();
};
```

**Get Agreement Status**:
```javascript
const getAgreementStatus = async (agreementId) => {
  const response = await fetch(
    `https://api.adobesign.com/api/rest/v6/agreements/${agreementId}`,
    {
      headers: {
        'Authorization': `Bearer ${signAccessToken}`
      }
    }
  );
  
  return response.json();
};

// Response
{
  "id": "CBJCHBCAABA...",
  "name": "Service Agreement",
  "status": "SIGNED",
  "createdDate": "2024-03-21T10:00:00Z",
  "expiration": "2024-04-21T10:00:00Z",
  "participantSets": [
    {
      "id": "PSET_123...",
      "memberInfos": [{
        "email": "signer@example.com",
        "status": "SIGNED",
        "signedDate": "2024-03-21T11:30:00Z"
      }]
    }
  ]
}
```

### Webhooks

**Register Webhook**:
```javascript
const registerWebhook = async () => {
  const response = await fetch('https://api.adobesign.com/api/rest/v6/webhooks', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${signAccessToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: "Agreement Events",
      scope: "ACCOUNT",
      state: "ACTIVE",
      webhookSubscriptionEvents: [
        "AGREEMENT_ALL",
        "AGREEMENT_CREATED",
        "AGREEMENT_SIGNED",
        "AGREEMENT_COMPLETED"
      ],
      webhookUrlInfo: {
        url: "https://your-app.com/webhook/adobe-sign"
      }
    })
  });
  
  return response.json();
};
```

## Acrobat AI Assistant API

### Document Analysis

**Ask Questions**:
```javascript
const askDocument = async (documentId, question) => {
  const response = await fetch(
    `https://pdf-services.adobe.io/operation/aiassistant/question`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
        'x-api-key': CLIENT_ID
      },
      body: JSON.stringify({
        documentId: documentId,
        question: question,
        citationFormat: 'formatted_text' // or 'json'
      })
    }
  );
  
  return response.json();
};

// Response
{
  "answer": "The contract specifies a 12-month term...",
  "citations": [
    {
      "page": 3,
      "text": "Term: This Agreement shall commence...",
      "boundingBox": { "x": 100, "y": 200, "width": 400, "height": 50 }
    }
  ],
  "confidence": 0.95
}
```

**Generate Summary**:
```javascript
const summarizeDocument = async (documentId) => {
  const response = await fetch(
    `https://pdf-services.adobe.io/operation/aiassistant/summarize`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
        'x-api-key': CLIENT_ID
      },
      body: JSON.stringify({
        documentId: documentId,
        summaryType: 'comprehensive', // or 'brief'
        includeKeyPoints: true
      })
    }
  );
  
  return response.json();
};
```

## API Limits & Pricing

### Rate Limits

| Operation | Free Tier | Paid Tier |
|-----------|-----------|-----------|
| PDF Operations | 1,000/month | Unlimited |
| Document Generation | 500/month | Unlimited |
| Extract PDF | 500/month | Unlimited |
| Acrobat Sign | 50 transactions | Unlimited |

### Pricing Model

**Pay-as-you-go**:
- PDF Services: $0.05 per transaction
- Document Generation: $0.10 per transaction
- Extract PDF: $0.10 per transaction
- Acrobat Sign: $1.50 per transaction

**Enterprise Plans**:
- Volume discounts available
- Custom SLAs
- Dedicated support

---

*Source: Adobe Document Cloud API Documentation, Acrobat Services Documentation*

            # 6. Emit event for async processing
            await self.events.emit(PaymentCompletedEvent(transaction))
            
            return PaymentResponse(success=True, transaction_id=transaction.id)
            
        except PaymentDeclined as e:
            await self.ledger.update(transaction.id, status=TransactionStatus.DECLINED)
            raise
        except Exception as e:
            await self.ledger.update(transaction.id, status=TransactionStatus.FAILED)
            await self.events.emit(PaymentFailedEvent(transaction, str(e)))
            raise
```

### 13.3 Database Schema Guidelines

```sql
-- Transactions table with proper indexing
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES accounts(id),
    amount DECIMAL(19,4) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    status VARCHAR(20) NOT NULL,
    type VARCHAR(20) NOT NULL,
    reference_id VARCHAR(100),
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_transactions_account ON transactions(account_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_created ON transactions(created_at);

-- Audit log for compliance
CREATE TABLE audit_logs (
    id BIGSERIAL PRIMARY KEY,
    entity_type VARCHAR(50) NOT NULL,
    entity_id UUID NOT NULL,
    action VARCHAR(50) NOT NULL,
    actor_id UUID NOT NULL,
    changes JSONB,
    ip_address INET,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 13.4 Error Response Standard

```json
{
  "error": {
    "code": "INSUFFICIENT_FUNDS",
    "message": "The account has insufficient funds for this transaction",
    "details": {
      "available": "100.00",
      "required": "150.00",
      "currency": "USD"
    },
    "trace_id": "req_abc123"
  }
}
```

### 13.5 Monitoring & Alerting

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Payment success rate | < 99.5% | PagerDuty |
| Average latency (p99) | > 500ms | Slack |
| Error rate | > 1% | PagerDuty |
| Queue depth | > 10000 | Slack |

### Trigger Words
- "fintech engineer"
- "digital banking"
- "payment systems"
- "blockchain"
- "API integration"
- "smart contract"
- "open banking"
- "PCI compliance"

### § 14 · Quality Verification

→ See references/standards.md §7.10 for full checklist

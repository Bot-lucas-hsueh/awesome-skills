            # 5. Update transaction status
            await self.ledger.update(
                transaction.id,
                status=TransactionStatus.COMPLETED,
                gateway_id=result.transaction_id
            )
            
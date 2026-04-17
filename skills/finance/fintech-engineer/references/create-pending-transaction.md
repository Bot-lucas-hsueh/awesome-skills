        # 3. Create pending transaction
        transaction = await self.ledger.create(
            amount=request.amount,
            currency=request.currency,
            status=TransactionStatus.PENDING
        )
        
        try:
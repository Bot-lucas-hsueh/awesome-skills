            # 4. Process with payment gateway
            result = await self.gateway.charge(
                token=request.payment_token,
                amount=request.amount,
                idempotency_key=request.idempotency_key
            )
            
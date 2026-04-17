        # 2. Check idempotency
        existing = await self.idempotency.check(request.idempotency_key)
        if existing:
            return existing
        
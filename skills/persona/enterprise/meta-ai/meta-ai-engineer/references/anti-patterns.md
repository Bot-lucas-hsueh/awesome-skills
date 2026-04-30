# Anti-Pattern Code Examples

## Anti-Pattern 1: Research Without Product Path

❌ "The model achieves SOTA on GLUE, let's publish"
✅ "The model achieves SOTA on GLUE AND improves Feed engagement by 2%; here's the PyTorch code"

## Anti-Pattern 2: Using JAX

❌ "Let's use JAX for this research project"
✅ "Stay in PyTorch; easier path to production and community adoption"

## Anti-Pattern 3: Premature Optimization

❌ "We'll optimize after proving the concept"
✅ "Quick unoptimized prototype → validated → then optimize with torch.compile"

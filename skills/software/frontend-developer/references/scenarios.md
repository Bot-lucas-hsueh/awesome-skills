## 9. Scenario Examples

### 9.1 Performance Optimization: LCP 5s → Under 2.5s

**User:** "我的 React 应用 Lighthouse 性能分 45，LCP 5 秒，怎么优化？"

**Frontend Developer:**
> **React 应用 LCP 优化行动计划**
>
> **Step 1: 识别 LCP 元素**
> ```bash
> # Chrome DevTools → Lighthouse → 找到 LCP 元素 (通常是 hero 图片)
> ```
>
> **Step 2: 图片优化 (LCP 最常见根因)**
> ```tsx
> // ❌ 旧方式: 无优化, 无尺寸提示, 无 preload
> <img src="/hero.jpg" alt="Hero" />
>
> // ✅ Next.js 项目
> import Image from 'next/image';
> <Image
>   src="/hero.jpg"
>   alt="Hero"
>   width={1200}
>   height={600}
>   priority                              // LCP 图片必须加 priority (自动 preload)
>   sizes="(max-width: 768px) 100vw, 1200px"
>   placeholder="blur"                    // 防止 CLS
> />
>
> // ✅ 非 Next.js 项目
> <link rel="preload" as="image" href="/hero.webp" fetchpriority="high" />
> <picture>
>   <source srcSet="/hero.avif" type="image/avif" />
>   <source srcSet="/hero.webp" type="image/webp" />
>   <img src="/hero.jpg" alt="Hero" width="1200" height="600" loading="eager" />
> </picture>
> ```
>
> **Step 3: 代码分割 (减少初始 bundle)**
> ```typescript
> // vite.config.ts — 添加 bundle 分析
> import { visualizer } from 'rollup-plugin-visualizer';
> export default { plugins: [visualizer({ open: true, gzipSize: true })] }
>
> // 路由级代码分割
> const Dashboard = lazy(() => import('./pages/Dashboard'));
> const Settings = lazy(() => import('./pages/Settings'));
>
> <Suspense fallback={<PageSkeleton />}>
>   <Routes>
>     <Route path="/dashboard" element={<Dashboard />} />
>   </Routes>
> </Suspense>
> ```
>
> **Step 4: 消除 CLS (布局偏移)**
> ```css
> img, video { aspect-ratio: attr(width)
> /* 始终为媒体元素指定尺寸; 动态内容用 min-height 预留空间 */
> ```
>
> **预期结果:** LCP 5s → 1.8s; Lighthouse 45 → 90+

### 9.2 State Management: Prop Drilling → Context + Zustand

**User:** "我的组件树 prop drilling 很严重，要把用户信息从根传到很深的子组件，怎么解决？"

**Frontend Developer:**
> **Prop Drilling 解决方案 — 按状态类型选择工具**
>
> **方案 1: React Context (认证信息 — 低频更新)**
> ```tsx
> interface AuthContextValue {
>   user: User | null;
>   isLoading: boolean;
> }
>
> const AuthContext = createContext<AuthContextValue | null>(null);
>
> export function AuthProvider({ children }: { children: ReactNode }) {
>   const { data: user, isLoading } = useQuery({
>     queryKey: ['auth', 'me'],
>     queryFn: () => fetch('/api/me').then(r => r.json()),
>   });
>   return <AuthContext.Provider value={{ user ?? null, isLoading }}>{children}</AuthContext.Provider>;
> }
>
> // 自定义 Hook — 比直接暴露 Context 更安全
> export function useAuth() {
>   const ctx = useContext(AuthContext);
>   if (!ctx) throw new Error('useAuth must be used within AuthProvider');
>   return ctx;
> }
>
> // 任何深度的子组件直接使用
> function UserAvatar() {
>   const { user } = useAuth();
>   return <img src={user?.avatar} alt={user?.name} />;
> }
> ```
>
> **方案 2: Zustand (全局客户端状态 — 高频更新)**
> ```tsx
> export const useCartStore = create<CartState>()(
>   persist(
>     (set, get) => ({
>       items: [],
>       addItem: (item) => set(state => ({ items: [...state.items, item] })),
>       total: () => get().items.reduce((sum, item) => sum + item.price, 0),
>     }),
>     { name: 'cart-storage' }
>   )
> );
>
> // 使用 selector 防止不必要 re-render
> const total = useCartStore(state => state.total());  // 只在 total 变化时 re-render
> ```
>
> **状态选型决策:**
> | 场景 | 推荐 |
> |------|------|
> | 当前用户信息 | Context + TanStack Query |
> | 购物车、全局通知 | Zustand + persist |
> | 表单状态 | React Hook Form (本地) |
> | 搜索过滤 | URL search params |

### 9.3 Accessibility: WCAG-Compliant Dropdown

**User:** "帮我实现一个无障碍的下拉菜单，需要支持键盘导航"

**Frontend Developer:**
> **WCAG AA 兼容 Dropdown — 推荐使用 Radix UI**
>
> **方案 1: Radix UI (自动处理 ARIA + 键盘)**
> ```tsx
> import * as DropdownMenu from '@radix-ui/react-dropdown-menu';
>
> function UserMenu({ user }: { user: User }) {
>   return (
>     <DropdownMenu.Root>
>       <DropdownMenu.Trigger asChild>
>         <button
>           className="flex items-center gap-2 rounded-lg p-2 hover:bg-gray-100 focus:ring-2"
>           aria-label={`User menu for ${user.name}`}
>         >
>           <img src={user.avatar} alt="" aria-hidden="true" className="h-8 w-8 rounded-full" />
>           <span>{user.name}</span>
>         </button>
>       </DropdownMenu.Trigger>
>       <DropdownMenu.Portal>
>         <DropdownMenu.Content className="min-w-48 rounded-lg bg-white shadow-lg border p-1" sideOffset={5}>
>           <DropdownMenu.Item className="rounded px-3 py-2 text-sm cursor-pointer hover:bg-gray-100 outline-none" onSelect={() => router.push('/profile')}>
>             Profile
>           </DropdownMenu.Item>
>           <DropdownMenu.Separator className="my-1 h-px bg-gray-200" />
>           <DropdownMenu.Item className="rounded px-3 py-2 text-sm text-red-600 cursor-pointer hover:bg-red-50 outline-none" onSelect={signOut}>
>             Sign Out
>           </DropdownMenu.Item>
>         </DropdownMenu.Content>
>       </DropdownMenu.Portal>
>     </DropdownMenu.Root>
>   );
> }
> // 自动支持: ↑↓ 键导航, Enter/Space 选择, Escape 关闭, focus trap
> ```
>
> **无障碍验证清单:**
> - [ ] Tab 到触发器: focus ring 可见
> - [ ] Enter/Space: 打开菜单
> - [ ] ↑↓ 键: 在菜单项间导航
> - [ ] Escape: 关闭菜单并返回触发器
> - [ ] VoiceOver/NVDA: 宣读 "menu" role 和每个 "menuitem"

### 9.4 Anti-Pattern Correction: useEffect Abuse

**User:** "我用 useEffect 来派生状态，用来计算过滤后的列表，对吗？"

**Frontend Developer:**
> **❌ 你描述的是一个常见 React 反模式**
>
> **问题: 用 useEffect 派生状态**
> ```tsx
> // ❌ BAD: 无必要的 useEffect — 创建额外的渲染周期
> function ProductList({ products, searchQuery }) {
>   const [filtered, setFiltered] = useState(products);
>
>   useEffect(() => {
>     setFiltered(products.filter(p => p.name.includes(searchQuery)));
>   }, [products, searchQuery]);
>
>   return <ul>{filtered.map(...)}</ul>;
> }
> // 问题: 每次 filter 触发 2 次渲染 (setState → render) + 闭包陷阱风险
> ```
>
> **✅ GOOD: 直接计算 — 零额外渲染**
> ```tsx
> function ProductList({ products, searchQuery }) {
>   // 在 render 中直接计算派生状态 — React 会 memoize 如果你需要
>   const filtered = products.filter(p => p.name.includes(searchQuery));
>
>   // 只有在 products 或 searchQuery 变化时才重新计算 (1000+ items 时考虑)
>   const filteredMemo = useMemo(
>     () => products.filter(p => p.name.includes(searchQuery)),
>     [products, searchQuery]
>   );
>
>   return <ul>{filtered.map(...)}</ul>;
> }
> ```
>
> **useEffect 适用场景 (仅这些):**
> - 外部系统同步 (WebSocket, DOM 事件, 浏览器 API)
> - 数据获取 (但推荐用 TanStack Query 替代)
> - 清理订阅或副作用
>
> **不适用场景:**
> - 派生状态 → 直接计算或 useMemo
> - 响应事件 → 事件处理器
> - 初始化数据 → TanStack Query initialData

---


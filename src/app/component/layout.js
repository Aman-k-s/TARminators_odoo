export default function Layout({ children }) {
  return (
    <div className="min-h-screen bg-gray-900 text-white px-4 py-6">
      <header className="text-2xl font-semibold mb-6">Skill Swap</header>
      <main>{children}</main>
    </div>
  );
}

import WelcomeHeader from "./WelcomeHeader.jsx";

// Main dashboard content region placeholder.
function MainContent() {
  return (
    <section className="space-y-6">
      <WelcomeHeader />

      <section className="min-h-[300px] rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        <div className="h-full rounded-xl bg-slate-50 p-4 text-sm text-slate-600">Main Content</div>
      </section>
    </section>
  );
}

export default MainContent;

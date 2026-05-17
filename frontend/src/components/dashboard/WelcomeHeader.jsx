import ActionButtons from "./ActionButtons.jsx";
import GreetingSection from "./GreetingSection.jsx";

// Dashboard welcome header to establish context and key actions.
function WelcomeHeader() {
  return (
    <section className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="flex flex-col items-start justify-between gap-4 lg:flex-row lg:items-center">
        <GreetingSection />
        <ActionButtons />
      </div>
    </section>
  );
}

export default WelcomeHeader;

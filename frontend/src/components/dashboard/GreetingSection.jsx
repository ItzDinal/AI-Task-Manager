import DateDisplay from "./DateDisplay.jsx";

// Left content block with greeting, date context, and motivational copy.
function GreetingSection() {
  return (
    <div className="min-w-0">
      <h1 className="text-2xl font-bold text-gray-900 sm:text-3xl">Good Morning, Dinal 👋</h1>
      <div className="mt-2">
        <DateDisplay />
      </div>
      <p className="mt-2 text-sm text-gray-500 sm:text-base">Let&apos;s make today productive and stress-free.</p>
    </div>
  );
}

export default GreetingSection;

// CTA button placeholder for entering focus mode.
function FocusModeButton() {
  return (
    <button
      type="button"
      className="w-full rounded-xl bg-black py-3 text-sm font-medium text-white transition-all duration-200 ease-in-out motion-safe:transform-gpu motion-safe:hover:scale-[1.01] hover:bg-gray-800 hover:shadow-sm"
    >
      Enter Focus Mode
    </button>
  );
}

export default FocusModeButton;

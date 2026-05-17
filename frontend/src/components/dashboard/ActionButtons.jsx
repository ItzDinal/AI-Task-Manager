// Primary and secondary dashboard quick actions.
function ActionButtons() {
  return (
    <div className="flex w-full flex-col gap-3 sm:w-auto sm:flex-row">
      <button
        type="button"
        className="rounded-xl bg-black px-5 py-3 text-sm font-medium text-white transition-all duration-200 hover:bg-gray-800"
      >
        + Add Task
      </button>
      <button
        type="button"
        className="rounded-xl border border-gray-200 bg-white px-5 py-3 text-sm font-medium text-gray-700 transition-all duration-200 hover:bg-gray-50"
      >
        View Analytics
      </button>
    </div>
  );
}

export default ActionButtons;

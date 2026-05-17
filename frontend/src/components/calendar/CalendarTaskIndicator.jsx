// Dot indicator for days with tasks.
function CalendarTaskIndicator({ hasTask }) {
  if (!hasTask) {
    return null;
  }

  return <span className="mt-1 inline-block h-1.5 w-1.5 rounded-full bg-gray-400" />;
}

export default CalendarTaskIndicator;

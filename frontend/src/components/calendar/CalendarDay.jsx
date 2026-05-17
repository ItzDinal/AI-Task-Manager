import CalendarTaskIndicator from "./CalendarTaskIndicator.jsx";

// Custom calendar day content with task indicators.
function CalendarDay({ date, hasTask }) {
  return (
    <div className="flex h-full w-full flex-col items-center justify-center">
      <span>{date.getDate()}</span>
      <CalendarTaskIndicator hasTask={hasTask} />
    </div>
  );
}

export default CalendarDay;

import { ChevronLeft, ChevronRight } from "lucide-react";

// Calendar header with month label and month navigation controls.
function CalendarHeader({ monthLabel, onPrevMonth, onNextMonth }) {
  return (
    <div className="flex items-center justify-between">
      <h3 className="text-lg font-semibold text-gray-900">{monthLabel}</h3>
      <div className="flex items-center gap-2">
        <button
          type="button"
          aria-label="Previous month"
          onClick={onPrevMonth}
          className="rounded-lg p-2 text-gray-600 transition-all duration-200 hover:bg-gray-100"
        >
          <ChevronLeft size={16} />
        </button>
        <button
          type="button"
          aria-label="Next month"
          onClick={onNextMonth}
          className="rounded-lg p-2 text-gray-600 transition-all duration-200 hover:bg-gray-100"
        >
          <ChevronRight size={16} />
        </button>
      </div>
    </div>
  );
}

export default CalendarHeader;

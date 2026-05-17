import { useMemo, useState } from "react";
import CalendarGrid from "./CalendarGrid.jsx";
import CalendarHeader from "./CalendarHeader.jsx";
import UpcomingEvents from "./UpcomingEvents.jsx";

const TASK_DAYS = [18, 20, 22];

// Compact calendar widget for date awareness and upcoming tasks.
function MiniCalendar() {
  const today = new Date();
  const [activeDate, setActiveDate] = useState(new Date(today.getFullYear(), today.getMonth(), 1));
  const [selectedDate, setSelectedDate] = useState(today);

  const monthLabel = activeDate.toLocaleDateString("en-US", {
    month: "long",
    year: "numeric",
  });

  const taskDates = useMemo(
    () => TASK_DAYS.map((day) => new Date(activeDate.getFullYear(), activeDate.getMonth(), day).toDateString()),
    [activeDate],
  );

  const handlePrevMonth = () => {
    setActiveDate((prev) => new Date(prev.getFullYear(), prev.getMonth() - 1, 1));
  };

  const handleNextMonth = () => {
    setActiveDate((prev) => new Date(prev.getFullYear(), prev.getMonth() + 1, 1));
  };

  return (
    <section className="flex flex-col gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm transition-all duration-200 ease-in-out hover:shadow-md">
      <CalendarHeader monthLabel={monthLabel} onPrevMonth={handlePrevMonth} onNextMonth={handleNextMonth} />

      <CalendarGrid
        activeDate={activeDate}
        selectedDate={selectedDate}
        onChangeDate={(value) => setSelectedDate(value)}
        onActiveStartDateChange={setActiveDate}
        taskDates={taskDates}
      />

      <UpcomingEvents />
    </section>
  );
}

export default MiniCalendar;

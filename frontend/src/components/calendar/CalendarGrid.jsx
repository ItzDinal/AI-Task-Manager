import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";
import CalendarDay from "./CalendarDay.jsx";

// Mini calendar grid powered by react-calendar with custom tile rendering.
function CalendarGrid({ activeDate, selectedDate, onChangeDate, onActiveStartDateChange, taskDates }) {
  const hasTaskOnDate = (date) => taskDates.includes(date.toDateString());

  return (
    <div className="calendar-widget overflow-hidden rounded-xl border border-gray-100 bg-white p-2">
      <Calendar
        value={selectedDate}
        activeStartDate={activeDate}
        onChange={onChangeDate}
        onActiveStartDateChange={({ activeStartDate }) => {
          if (activeStartDate) {
            onActiveStartDateChange(activeStartDate);
          }
        }}
        prevLabel={null}
        nextLabel={null}
        prev2Label={null}
        next2Label={null}
        showNavigation={false}
        formatShortWeekday={(_, date) => date.toLocaleDateString("en-US", { weekday: "narrow" })}
        tileContent={({ date, view }) =>
          view === "month" ? <CalendarDay date={date} hasTask={hasTaskOnDate(date)} /> : null
        }
        tileClassName={({ date, view }) => {
          if (view !== "month") {
            return "";
          }

          const isToday = date.toDateString() === new Date().toDateString();
          const isSelected = date.toDateString() === selectedDate.toDateString();
          const isNeighbor = date.getMonth() !== activeDate.getMonth();

          if (isSelected || isToday) {
            return "calendar-tile-selected";
          }

          if (isNeighbor) {
            return "calendar-tile-muted";
          }

          return "calendar-tile-default";
        }}
      />
    </div>
  );
}

export default CalendarGrid;

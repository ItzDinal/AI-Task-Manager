// Upcoming tasks preview under the mini calendar.
function UpcomingEvents() {
  const upcomingItems = [
    { id: 1, title: "Team Meeting", date: "May 18" },
    { id: 2, title: "UI Review", date: "May 20" },
    { id: 3, title: "Project Deadline", date: "May 22" },
  ];

  return (
    <section className="space-y-2">
      <p className="text-xs uppercase tracking-wide text-gray-400">Upcoming Tasks</p>
      <div className="space-y-2">
        {upcomingItems.map((item) => (
          <div key={item.id} className="flex items-center justify-between rounded-xl bg-gray-50 px-3 py-2">
            <span className="text-sm text-gray-700">{item.title}</span>
            <span className="text-xs text-gray-500">{item.date}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

export default UpcomingEvents;

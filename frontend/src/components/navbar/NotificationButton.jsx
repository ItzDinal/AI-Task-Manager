import { Bell } from "lucide-react";

// Notification action with unread indicator placeholder.
function NotificationButton() {
  return (
    <button
      type="button"
      aria-label="Notifications"
      className="relative inline-flex h-10 w-10 items-center justify-center rounded-xl text-gray-600 transition duration-200 hover:bg-gray-100"
    >
      <Bell size={18} />
      <span className="absolute top-2 right-2 h-2 w-2 rounded-full bg-black" />
    </button>
  );
}

export default NotificationButton;

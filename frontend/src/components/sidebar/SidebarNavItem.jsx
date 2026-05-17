import { NavLink } from "react-router-dom";

// Reusable navigation item with icon and active state styling.
function SidebarNavItem({ to, icon: Icon, label, onClick }) {
  return (
    <NavLink
      to={to}
      onClick={onClick}
      className={({ isActive }) =>
        `flex items-center gap-3 rounded-xl px-4 py-3 text-sm transition-all duration-200 ${
          isActive ? "bg-black text-white" : "text-gray-600 hover:bg-gray-100"
        }`
      }
    >
      <Icon size={18} />
      <span className="font-medium">{label}</span>
    </NavLink>
  );
}

export default SidebarNavItem;

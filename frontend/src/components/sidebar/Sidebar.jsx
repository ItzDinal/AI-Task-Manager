import { X } from "lucide-react";
import ProjectList from "./ProjectList.jsx";
import SidebarHeader from "./SidebarHeader.jsx";
import SidebarNav from "./SidebarNav.jsx";
import TagList from "./TagList.jsx";
import UpgradeCard from "./UpgradeCard.jsx";
import UserProfileCard from "./UserProfileCard.jsx";

// Dashboard sidebar shell with desktop and mobile-drawer behavior.
function Sidebar({ isOpen = false, onClose }) {
  return (
    <>
      <button
        type="button"
        aria-label="Close sidebar overlay"
        onClick={onClose}
        className={`fixed inset-0 z-30 bg-black/30 transition-opacity duration-200 lg:hidden ${
          isOpen ? "pointer-events-auto opacity-100" : "pointer-events-none opacity-0"
        }`}
      />

      <aside
        className={`fixed top-0 left-0 z-40 h-screen w-64 shrink-0 border-r border-gray-200 bg-white p-4 transition-transform duration-300 lg:sticky lg:z-auto lg:block lg:translate-x-0 ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="flex h-full flex-col gap-4">
          <div className="flex items-center justify-between lg:block">
            <SidebarHeader />
            <button
              type="button"
              onClick={onClose}
              aria-label="Close sidebar"
              className="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200 text-gray-600 transition-all duration-200 hover:bg-gray-100 lg:hidden"
            >
              <X size={16} />
            </button>
          </div>

          <div className="flex-1 space-y-4 overflow-y-auto pr-1">
            <SidebarNav onItemClick={onClose} />
            <ProjectList />
            <TagList />
            <UpgradeCard />
          </div>
          <UserProfileCard />
        </div>
      </aside>
    </>
  );
}

export default Sidebar;

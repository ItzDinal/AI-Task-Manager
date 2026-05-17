import SidebarHeader from "./SidebarHeader.jsx";
import SidebarNav from "./SidebarNav.jsx";
import ProjectList from "./ProjectList.jsx";
import TagList from "./TagList.jsx";
import UpgradeCard from "./UpgradeCard.jsx";
import UserProfileCard from "./UserProfileCard.jsx";

// Dashboard sidebar shell prepared for desktop and future mobile drawer.
function Sidebar() {
  return (
    <aside className="sticky top-0 hidden h-screen w-64 shrink-0 border-r border-gray-200 bg-white p-4 lg:block">
      <div className="flex h-full flex-col gap-4">
        <SidebarHeader />
        <div className="flex-1 space-y-4 overflow-y-auto pr-1">
          <SidebarNav />
          <ProjectList />
          <TagList />
          <UpgradeCard />
        </div>
        <UserProfileCard />
      </div>
    </aside>
  );
}

export default Sidebar;

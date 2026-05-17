import MobileMenuButton from "./MobileMenuButton.jsx";
import NavbarSearch from "./NavbarSearch.jsx";
import NotificationButton from "./NotificationButton.jsx";
import QuickActionButton from "./QuickActionButton.jsx";
import ThemeToggle from "./ThemeToggle.jsx";
import UserMenu from "./UserMenu.jsx";

// Top-level dashboard navbar with responsive productivity actions.
function TopNavbar({ onOpenSidebar }) {
  return (
    <header className="h-16 border-b border-gray-200 bg-white px-3 sm:px-4 lg:px-6">
      <div className="flex h-full items-center justify-between gap-2 sm:gap-3">
        <div className="flex min-w-0 items-center gap-2 sm:gap-3">
          <MobileMenuButton onClick={onOpenSidebar} />
          <div className="min-w-0">
            <p className="truncate text-sm font-semibold text-gray-900 sm:text-base">Dashboard</p>
            <p className="hidden truncate text-xs text-gray-400 md:block">Workspace / Overview</p>
          </div>
        </div>

        <div className="hidden flex-1 justify-center px-2 lg:flex">
          <NavbarSearch />
        </div>

        <div className="flex shrink-0 items-center gap-1.5 sm:gap-2">
          <div className="w-24 sm:w-40 lg:hidden">
            <NavbarSearch />
          </div>
          <NotificationButton />
          <QuickActionButton />
          <div className="hidden sm:block">
            <ThemeToggle />
          </div>
          <div className="hidden md:block">
            <UserMenu />
          </div>
        </div>
      </div>
    </header>
  );
}

export default TopNavbar;

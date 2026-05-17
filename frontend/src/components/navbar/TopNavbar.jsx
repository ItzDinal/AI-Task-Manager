import MobileMenuButton from "./MobileMenuButton.jsx";
import NavbarSearch from "./NavbarSearch.jsx";
import NotificationButton from "./NotificationButton.jsx";
import QuickActionButton from "./QuickActionButton.jsx";
import ThemeToggle from "./ThemeToggle.jsx";
import UserMenu from "./UserMenu.jsx";

// Top-level dashboard navbar with responsive productivity actions.
function TopNavbar() {
  return (
    <header className="h-16 border-b border-gray-200 bg-white px-4 sm:px-6">
      <div className="flex h-full items-center justify-between gap-3">
        <div className="flex min-w-0 items-center gap-3">
          <MobileMenuButton />
          <div className="min-w-0">
            <p className="truncate text-sm font-semibold text-gray-900">Dashboard</p>
            <p className="hidden truncate text-xs text-gray-400 md:block">Workspace / Overview</p>
          </div>
        </div>

        <div className="hidden flex-1 justify-center px-2 lg:flex">
          <NavbarSearch />
        </div>

        <div className="flex shrink-0 items-center gap-2 sm:gap-3">
          <div className="w-28 sm:w-44 lg:hidden">
            <NavbarSearch />
          </div>
          <NotificationButton />
          <QuickActionButton />
          <ThemeToggle />
          <UserMenu />
        </div>
      </div>
    </header>
  );
}

export default TopNavbar;

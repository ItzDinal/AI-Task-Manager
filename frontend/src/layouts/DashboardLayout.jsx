import { useEffect, useState } from "react";
import Sidebar from "../components/sidebar/Sidebar.jsx";
import TopNavbar from "../components/navbar/TopNavbar.jsx";
import MainContent from "../components/dashboard/MainContent.jsx";
import RightPanel from "../components/dashboard/RightPanel.jsx";

// Dashboard shell layout with sidebar, top nav, and adaptive content grid.
function DashboardLayout() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  useEffect(() => {
    if (isSidebarOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }

    return () => {
      document.body.style.overflow = "";
    };
  }, [isSidebarOpen]);

  return (
    <div className="min-h-screen bg-[#f5f7fb]">
      <div className="mx-auto flex min-h-screen max-w-[1600px]">
        <Sidebar isOpen={isSidebarOpen} onClose={() => setIsSidebarOpen(false)} />

        <section className="flex min-h-screen min-w-0 flex-1 flex-col">
          <TopNavbar onOpenSidebar={() => setIsSidebarOpen(true)} />

          <div className="grid flex-1 grid-cols-1 gap-4 p-4 sm:gap-6 sm:p-6 xl:grid-cols-[minmax(0,1fr)_320px]">
            <MainContent />
            <RightPanel />
          </div>
        </section>
      </div>
    </div>
  );
}

export default DashboardLayout;

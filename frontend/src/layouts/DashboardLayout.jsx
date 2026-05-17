import Sidebar from "../components/sidebar/Sidebar.jsx";
import TopNavbar from "../components/navbar/TopNavbar.jsx";
import MainContent from "../components/dashboard/MainContent.jsx";
import RightPanel from "../components/dashboard/RightPanel.jsx";

// Dashboard shell layout with sidebar, top nav, and two-column body.
function DashboardLayout() {
  return (
    <div className="min-h-screen bg-[#f5f7fb]">
      <div className="mx-auto flex min-h-screen max-w-[1600px]">
        <Sidebar />

        <section className="flex min-h-screen min-w-0 flex-1 flex-col">
          <TopNavbar />

          <div className="grid flex-1 grid-cols-1 gap-6 p-6 xl:grid-cols-[minmax(0,1fr)_320px]">
            <MainContent />
            <div className="hidden xl:block">
              <RightPanel />
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default DashboardLayout;

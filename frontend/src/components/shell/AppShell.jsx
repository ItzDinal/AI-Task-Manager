import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

const AppShell = ({ title, children }) => {
  return (
    <div className="min-h-screen bg-[#edf2f7]">
      <div className="mx-auto flex min-h-screen max-w-[1440px] border-x border-slate-200/80 bg-white shadow-[0_10px_40px_rgba(15,23,42,0.06)]">
        <Sidebar />
        <div className="flex min-h-screen flex-1 flex-col">
          <Topbar title={title} />
          <main className="flex-1 bg-gradient-to-b from-slate-50 to-slate-100/70 p-6">{children}</main>
        </div>
      </div>
    </div>
  );
};

export default AppShell;

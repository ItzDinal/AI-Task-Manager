import { Outlet } from "react-router-dom";

const FocusLayout = () => {
  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <div className="mx-auto max-w-4xl">
        <Outlet />
      </div>
    </div>
  );
};

export default FocusLayout;

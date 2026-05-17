import { Navigate, Route, Routes } from "react-router-dom";
import MainLayout from "../layouts/MainLayout";
import FocusLayout from "../layouts/FocusLayout";
import DashboardPage from "../pages/DashboardPage";
import Tasks from "../pages/Tasks";
import Focus from "../pages/Focus";
import Analytics from "../pages/Analytics";
import DailyPlan from "../pages/DailyPlan";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/dashboard" element={<DashboardPage />} />
      <Route element={<MainLayout />}>
        <Route path="/tasks" element={<Tasks />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/daily-plan" element={<DailyPlan />} />
      </Route>
      <Route element={<FocusLayout />}>
        <Route path="/focus" element={<Focus />} />
      </Route>
      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
};

export default AppRoutes;

import { Navigate, Route, Routes } from "react-router-dom";
import WireframeLoginPage from "./pages/wireframe/WireframeLoginPage";
import WireframeDashboardPage from "./pages/wireframe/WireframeDashboardPage";
import WireframeTaskManagementPage from "./pages/wireframe/WireframeTaskManagementPage";
import WireframeFocusModePage from "./pages/wireframe/WireframeFocusModePage";
import WireframeAnalyticsPage from "./pages/wireframe/WireframeAnalyticsPage";
import WireframeDailyPlanPage from "./pages/wireframe/WireframeDailyPlanPage";
import WireframeAddTaskPage from "./pages/wireframe/WireframeAddTaskPage";
import WireframeSummaryPage from "./pages/wireframe/WireframeSummaryPage";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<WireframeLoginPage />} />
      <Route path="/dashboard" element={<WireframeDashboardPage />} />
      <Route path="/tasks" element={<WireframeTaskManagementPage />} />
      <Route path="/focus" element={<WireframeFocusModePage />} />
      <Route path="/analytics" element={<WireframeAnalyticsPage />} />
      <Route path="/daily-plan" element={<WireframeDailyPlanPage />} />
      <Route path="/task-modal" element={<WireframeAddTaskPage />} />
      <Route path="/summary" element={<WireframeSummaryPage />} />
      <Route path="/calendar" element={<WireframeDashboardPage />} />
      <Route path="/settings" element={<WireframeDashboardPage />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
}

export default App;

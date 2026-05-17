import AIHeader from "./AIHeader.jsx";
import AIInsightCard from "./AIInsightCard.jsx";
import AITypingIndicator from "./AITypingIndicator.jsx";
import FocusRecommendation from "./FocusRecommendation.jsx";
import QuickAIActions from "./QuickAIActions.jsx";
import SuggestedTasks from "./SuggestedTasks.jsx";

// Premium AI productivity assistant widget for focus and task clarity.
function AIAssistantWidget() {
  return (
    <section className="flex flex-col gap-5 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm transition-all duration-200 ease-in-out hover:shadow-md">
      <AIHeader />
      <AIInsightCard />
      <FocusRecommendation />
      <SuggestedTasks />
      <QuickAIActions />
      <AITypingIndicator />
    </section>
  );
}

export default AIAssistantWidget;

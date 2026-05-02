import AuthLayout from "../components/layout/AuthLayout";
import LoginCard from "../components/auth/LoginCard";
import ProgressBar from "../components/ui/ProgressBar";

const Login = () => {
  return (
    <AuthLayout
      left={
        <div className="mx-auto w-full max-w-md lg:max-w-lg">
          <h1 className="text-5xl font-bold leading-none tracking-tight text-[#1f2d44] lg:text-7xl">
            Wisen<span className="text-cyan-500">Task</span>
          </h1>

          <h2 className="mt-8 text-4xl font-semibold leading-tight text-[#0f2d57] lg:text-5xl">
            AI Task Manager
          </h2>

          <p className="mt-4 text-xl text-[#35557f] lg:text-3xl">Focus better. Achieve more.</p>

          <div className="mt-14 max-w-md space-y-6">
            <ProgressBar label="Task completion" value={87} />
            <ProgressBar label="Focus sessions" value={62} />
            <ProgressBar label="Weekly goals" value={94} />
          </div>
        </div>
      }
      right={<LoginCard />}
    />
  );
};

export default Login;

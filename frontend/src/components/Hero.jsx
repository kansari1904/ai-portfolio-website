const Hero = () => {
    return (
        <section
            id="home"
            className="relative overflow-hidden bg-slate-950 pt-25 pb-20 sm:pt-36 sm:pb-24 lg:pt-20 lg:pb-28"
        >
            {/* Subtle background glow */}
            <div className="pointer-events-none absolute left-1/2 top-20 -z-0 h-72 w-72 -translate-x-1/2 rounded-full bg-blue-500/10 blur-3xl" />

            <div className="relative z-10 mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="mx-auto max-w-4xl text-center">

                    {/* Availability */}
                    <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-slate-800 bg-slate-900/70 px-4 py-2 text-sm text-slate-300">
                        <span className="h-2 w-2 rounded-full bg-emerald-400" />
                        Open to opportunities
                    </div>

                    {/* Heading */}
                    <h1 className="text-4xl font-bold tracking-tight text-white sm:text-5xl lg:text-6xl">
                        Hi, I'm{" "}
                        <span className="text-slate-300">
                            Khalid Ansari
                        </span>
                    </h1>

                    {/* Role */}
                    <p className="mt-5 text-xl font-medium text-blue-400 sm:text-2xl">
                        Software Engineer · AI Engineer
                    </p>

                    {/* Description */}
                    <p className="mx-auto mt-6 max-w-2xl text-base leading-7 text-slate-400 sm:text-lg sm:leading-8">
                        I build modern web applications and AI-powered systems using
                        technologies like React, FastAPI, LLM APIs, RAG, and agentic
                        workflows.
                    </p>

                    {/* Actions */}
                    <div className="mt-9 flex flex-col items-center justify-center gap-4 sm:flex-row">
                        <a
                            href="#projects"
                            className="w-full rounded-lg bg-white px-6 py-3 text-sm font-semibold text-slate-950 transition hover:bg-slate-200 sm:w-auto"
                        >
                            View Projects
                        </a>

                        <a
                            href="#chat"
                            className="w-full rounded-lg border border-slate-700 bg-slate-900 px-6 py-3 text-sm font-semibold text-white transition hover:border-slate-600 hover:bg-slate-800 sm:w-auto"
                        >
                            Ask My AI Assistant
                        </a>
                    </div>

                    {/* Quick highlights */}
                    <div className="mt-14 grid grid-cols-1 gap-4 sm:grid-cols-3">

                        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-5">
                            <p className="text-2xl font-bold text-white">
                                AI
                            </p>
                            <p className="mt-1 text-sm text-slate-400">
                                LLM & Agentic Systems
                            </p>
                        </div>

                        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-5">
                            <p className="text-2xl font-bold text-white">
                                Full Stack
                            </p>
                            <p className="mt-1 text-sm text-slate-400">
                                React & Backend Development
                            </p>
                        </div>

                        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-5">
                            <p className="text-2xl font-bold text-white">
                                RAG
                            </p>
                            <p className="mt-1 text-sm text-slate-400">
                                Retrieval-Augmented AI
                            </p>
                        </div>

                    </div>
                </div>
            </div>
        </section>
    );
};

export default Hero;
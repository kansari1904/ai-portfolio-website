const About = () => {
    return (
        <section
            id="about"
            className="border-t border-slate-900 bg-slate-950 py-20 sm:py-24"
        >
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="grid gap-12 lg:grid-cols-2 lg:items-center">

                    {/* Introduction */}
                    <div>
                        <p className="text-sm font-semibold uppercase tracking-wider text-blue-400">
                            About Me
                        </p>

                        <h2 className="mt-3 text-3xl font-bold tracking-tight text-white sm:text-4xl">
                            Building software with AI at the center.
                        </h2>

                        <p className="mt-6 text-base leading-7 text-slate-400">
                            I'm Khalid Ansari, a Computer Science and Engineering graduate
                            focused on software development and AI engineering. I enjoy
                            building practical applications that combine modern web
                            technologies with AI capabilities.
                        </p>

                        <p className="mt-4 text-base leading-7 text-slate-400">
                            My current focus includes LLM applications, Retrieval-Augmented
                            Generation, AI agents, FastAPI backends, and full-stack
                            development with React.
                        </p>
                    </div>

                    {/* Focus Areas */}
                    <div className="grid gap-4 sm:grid-cols-2">

                        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6">
                            <h3 className="font-semibold text-white">
                                AI Engineering
                            </h3>

                            <p className="mt-2 text-sm leading-6 text-slate-400">
                                Building LLM-powered applications, RAG pipelines, and
                                agentic workflows.
                            </p>
                        </div>

                        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6">
                            <h3 className="font-semibold text-white">
                                Full Stack
                            </h3>

                            <p className="mt-2 text-sm leading-6 text-slate-400">
                                Developing responsive interfaces and scalable backend APIs.
                            </p>
                        </div>

                        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6">
                            <h3 className="font-semibold text-white">
                                Problem Solving
                            </h3>

                            <p className="mt-2 text-sm leading-6 text-slate-400">
                                Strengthening software engineering fundamentals through
                                data structures and algorithms.
                            </p>
                        </div>

                        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6">
                            <h3 className="font-semibold text-white">
                                Continuous Learning
                            </h3>

                            <p className="mt-2 text-sm leading-6 text-slate-400">
                                Exploring modern AI engineering tools and production
                                development practices.
                            </p>
                        </div>

                    </div>
                </div>
            </div>
        </section>
    );
};

export default About;
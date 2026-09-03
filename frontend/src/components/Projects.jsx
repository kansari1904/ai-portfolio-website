const projects = [
  {
    title: "DocuMind-AI",
    category: "AI / LLM Application",
    description:
      "An AI-powered document assistant that lets users upload PDFs, generate summaries, flashcards and quizzes, and interact with documents through an LLM-powered chat interface.",
    technologies: [
      "React",
      "Tailwind CSS",
      "Node.js",
      "Express",
      "MongoDB",
      "Gemini API",
    ],
    highlights: [
      "PDF document processing",
      "LLM-powered chat",
      "Automatic summaries, quizzes and flashcards",
    ],
  },
  {
    title: "AI Customer Support Agent",
    category: "AI Engineering",
    description:
      "An AI customer support system designed to answer user queries using knowledge retrieval, LLMs, and structured application workflows.",
    technologies: [
      "Python",
      "FastAPI",
      "RAG",
      "LangChain",
      "LLM APIs",
      "Vector Database",
    ],
    highlights: [
      "Retrieval-Augmented Generation",
      "Context-aware responses",
      "AI-powered support workflow",
    ],
  },
  {
    title: "CodeGyan",
    category: "Full Stack",
    description:
      "A full-stack e-learning platform where users can explore educational content through a modern web interface backed by a RESTful backend.",
    technologies: [
      "React",
      "Node.js",
      "Express",
      "MongoDB",
      "Redux Toolkit",
      "Tailwind CSS",
    ],
    highlights: [
      "Full-stack MERN architecture",
      "Responsive React interface",
      "REST API integration",
    ],
  },
];

const Projects = () => {
  return (
    <section
      id="projects"
      className="border-t border-slate-900 bg-slate-950 py-20 sm:py-24"
    >
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="max-w-2xl">
          <p className="text-xs font-semibold uppercase tracking-[0.2em] text-blue-400 sm:text-sm">
            Selected Work
          </p>

          <h2 className="mt-3 text-3xl font-bold tracking-tight text-white sm:text-4xl">
            Projects I've built
          </h2>

          <p className="mt-4 text-sm leading-6 text-slate-400 sm:text-base">
            A selection of projects demonstrating my experience across
            AI engineering, full-stack development, and modern web
            application development.
          </p>
        </div>

        {/* Project Cards */}
        <div className="mt-10 grid gap-5 lg:grid-cols-3">
          {projects.map((project) => (
            <article
              key={project.title}
              className="group flex h-full flex-col rounded-2xl border border-slate-800 bg-slate-900/30 p-6 transition-all duration-300 hover:-translate-y-1 hover:border-slate-700 hover:bg-slate-900/60"
            >
              {/* Project Top */}
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className="text-xs font-medium uppercase tracking-wider text-blue-400">
                    {project.category}
                  </p>

                  <h3 className="mt-2 text-xl font-semibold text-white">
                    {project.title}
                  </h3>
                </div>

                <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-slate-800 bg-slate-950 text-slate-500 transition-colors group-hover:border-slate-700 group-hover:text-blue-400">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.8"
                    className="h-4 w-4"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M13 3h8v8"
                    />
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M10 14L21 3"
                    />
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M21 13v5a3 3 0 01-3 3H6a3 3 0 01-3-3V6a3 3 0 013-3h5"
                    />
                  </svg>
                </div>
              </div>

              {/* Description */}
              <p className="mt-5 text-sm leading-6 text-slate-400">
                {project.description}
              </p>

              {/* Highlights */}
              <div className="mt-6">
                <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
                  Key highlights
                </p>

                <ul className="mt-3 space-y-2">
                  {project.highlights.map((highlight) => (
                    <li
                      key={highlight}
                      className="flex items-start gap-2 text-sm text-slate-300"
                    >
                      <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-blue-400" />
                      <span>{highlight}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Technologies */}
              <div className="mt-auto pt-7">
                <div className="flex flex-wrap gap-2">
                  {project.technologies.map((technology) => (
                    <span
                      key={technology}
                      className="rounded-md border border-slate-800 bg-slate-950 px-2.5 py-1 text-xs text-slate-400"
                    >
                      {technology}
                    </span>
                  ))}
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Projects;
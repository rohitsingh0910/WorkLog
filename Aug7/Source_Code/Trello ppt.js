import React, { useState, useEffect } from 'react';

const slidesData = [
  {
    title: 'Trello: An Introduction',
    content: `
      Trello is a visual collaboration tool that organizes your projects into boards.
      Inspired by the Kanban system, it allows you to see what's being worked on, who is working on it, and what's next.
      It provides a simple, flexible, and powerful way to manage any project or workflow.
    `,
    image: null,
  },
  {
    title: 'Why Use Trello? Benefits for Software Teams',
    content: `
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Enhanced Visibility:</strong> Trello boards provide a high-level overview of a project's status, helping teams quickly understand the workflow and identify bottlenecks.</li>
        <li><strong>Efficient Workflow:</strong> The "To-Do," "Doing," "Done" structure enables a smooth, visual flow of tasks from one stage to the next.</li>
        <li><strong>Improved Collaboration:</strong> A shared workspace with comments, mentions, and activity logs keeps everyone on the same page and reduces the need for constant status meetings.</li>
        <li><strong>Agile-Friendly:</strong> Trello's flexibility makes it a perfect fit for Agile methodologies like Scrum and Kanban, allowing teams to manage sprints and backlogs effectively.</li>
      </ul>
    `,
    image: null,
  },
  {
    title: 'Trello Core Concepts: Boards, Lists, Cards',
    content: `
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Boards:</strong> The main workspace for a project. Think of a board as a whiteboard for your project.</li>
        <li><strong>Lists:</strong> Columns on a board that represent a stage in a workflow (e.g., "Backlog," "In Progress," "Completed").</li>
        <li><strong>Cards:</strong> The fundamental units of a board. A card represents a single task or idea and can be moved between lists.</li>
      </ul>
    `,
    image: null,
  },
  {
    title: 'Creating Your First Board',
    content: `
      <p>Creating a new Trello board is the first step to organizing your work. You can start from scratch or use one of Trello's many templates.</p>
      <p><strong>Steps:</strong></p>
      <ol class="list-decimal list-inside space-y-1">
        <li>Navigate to your workspace and click "Create new board."</li>
        <li>Give your board a descriptive title.</li>
        <li>Choose a background or color.</li>
        <li>Set the board's visibility (e.g., Workspace, Private).</li>
      </ol>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/15a8998d-2e28-44cd-984f-38a6d43ca2d0',
      alt: 'Creating a Trello board',
      width: 'w-2/3',
    },
  },
  {
    title: 'Managing Tasks with Cards (To-Do → Doing → Done)',
    content: `
      <p>The beauty of Trello lies in the ability to visually track tasks. As a task progresses, you simply drag and drop the card to the next list. This is the core of the Kanban workflow.</p>
      <p><strong>Example Workflow:</strong></p>
      <ul class="list-disc list-inside space-y-1">
        <li>A new task is added to the "To Do" list.</li>
        <li>A team member starts working on the task and moves the card to the "Doing" list.</li>
        <li>Once the task is complete, they move the card to the "Done" list.</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/015a64b4-07e3-469d-b192-cca3ed03fdb5',
      alt: 'Trello board with To Do, Doing, and Done lists',
      width: 'w-2/3',
    },
  },
  {
    title: 'Adding Checklists, Attachments & Labels',
    content: `
      <p>Cards can hold a wealth of information. You can enrich a card to add more detail and context.</p>
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Checklists:</strong> Break down large tasks into smaller, manageable sub-tasks.</li>
        <li><strong>Attachments:</strong> Add files, images, or links to a card for easy access to all relevant documents.</li>
        <li><strong>Labels:</strong> Categorize cards with different colors and titles (e.g., "Bug," "Feature," "Urgent," "Marketing").</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/2830e12a-8742-4575-b3d0-6f127a14109b',
      alt: 'Trello card with a description',
      width: 'w-2/3',
    },
  },
  {
    title: 'Setting Deadlines, Reminders & Due Dates',
    content: `
      <p>Keeping track of deadlines is crucial. Trello's date functionality helps you stay on schedule.</p>
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Due Dates:</strong> Set a specific date and time for a card to be completed.</li>
        <li><strong>Reminders:</strong> Trello automatically sends notifications as a deadline approaches.</li>
        <li><strong>Calendar View:</strong> The Calendar Power-Up lets you visualize all your cards with due dates in a calendar format.</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/290fdc14-98f1-4dbe-84e3-c1a321da156d',
      alt: 'Trello card with a due date',
      width: 'w-2/3',
    },
  },
  {
    title: 'Team Collaboration & Comments',
    content: `
      <p>Communication is key to any successful project. Trello's collaboration features are built directly into each card.</p>
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Comments:</strong> Use the comment section to discuss tasks, ask questions, or provide updates.</li>
        <li><strong>Mentions:</strong> Use the @ symbol to mention a team member and send them a notification directly.</li>
        <li><strong>Activity Log:</strong> The activity feed on each card tracks all changes and comments, providing a full history of the task.</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/2830e12a-8742-4575-b3d0-6f127a14109b',
      alt: 'Trello card with comments',
      width: 'w-2/3',
    },
  },
  {
    title: 'Using Power-Ups (e.g., Calendar, GitHub)',
    content: `
      <p>Power-Ups are Trello's way of integrating with other services to extend its functionality.</p>
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Calendar:</strong> Displays all cards with due dates on a calendar.</li>
        <li><strong>GitHub:</strong> Connects your Trello cards to GitHub pull requests and issues.</li>
        <li><strong>Custom Fields:</strong> Add custom data fields to your cards.</li>
        <li><strong>Others:</strong> Integrations with Slack, Jira, Drive, and many more.</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/582d883d-d9e6-414d-a4bc-6e949c6275cf',
      alt: 'Trello Power-Ups screen',
      width: 'w-2/3',
    },
  },
  {
    title: 'Trello for Sprint Planning (Agile Workflow)',
    content: `
      <p>Trello is an excellent tool for Agile teams. The columns can be configured to match a sprint's workflow.</p>
      <p><strong>Typical Agile Lists:</strong></p>
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Backlog:</strong> All the tasks for the project.</li>
        <li><strong>Sprint Backlog:</strong> Tasks selected for the current sprint.</li>
        <li><strong>In Progress:</strong> Tasks currently being worked on by the team.</li>
        <li><strong>Done:</strong> Completed tasks.</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/966062c6-0caa-4fe1-aa72-f60c7ef1a3ae',
      alt: 'Trello Agile Sprint Board Template',
      width: 'w-2/3',
    },
  },
  {
    title: 'Tracking Progress with Butler Automation',
    content: `
      <p>Butler is Trello's built-in automation tool. It allows you to create rules that automatically perform actions based on triggers.</p>
      <p><strong>Examples:</strong></p>
      <ul class="list-disc list-inside space-y-2">
        <li>Move a card to "Done" when a checklist is completed.</li>
        <li>Set a due date automatically when a card is moved to "In Progress."</li>
        <li>Archive cards that have been in "Done" for more than a week.</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/88ab1c7a-bca9-437c-97b9-bf66cd2eb949',
      alt: 'Trello Butler automation screen',
      width: 'w-2/3',
    },
  },
  {
    title: 'Templates and Board Sharing',
    content: `
      <p>Trello makes it easy to save and share your best workflows.</p>
      <ul class="list-disc list-inside space-y-2">
        <li><strong>Templates:</strong> Create templates from existing boards to reuse successful workflows for new projects.</li>
        <li><strong>Board Sharing:</strong> Share a board with team members by email or by generating a shareable link. You can also make a board public, so anyone can view it.</li>
      </ul>
    `,
    image: {
      src: 'https://storage.googleapis.com/g-e5b37628-89c6-4cb6-9a52-67063d3febfb/15a8998d-2e28-44cd-984f-38a6d43ca2d0',
      alt: 'Share Trello board dialog',
      width: 'w-2/3',
    },
  },
];

const App = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev < slidesData.length - 1 ? prev + 1 : prev));
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev > 0 ? prev - 1 : prev));
  };

  const handleKeyDown = (e) => {
    if (e.key === 'ArrowRight') {
      nextSlide();
    } else if (e.key === 'ArrowLeft') {
      prevSlide();
    }
  };

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  const slide = slidesData[currentSlide];

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-gray-100 p-4 font-sans">
      <div className="relative w-full max-w-5xl h-full bg-gray-800 rounded-2xl shadow-2xl overflow-hidden transition-all duration-500 transform scale-95 md:scale-100">
        <div className="flex flex-col items-center justify-center p-8 md:p-12 h-full">
          {/* Slide Content */}
          <div className="flex-grow flex flex-col items-center justify-center text-center w-full transition-opacity duration-500">
            <h1 className="text-3xl md:text-5xl font-extrabold mb-6 text-indigo-400">{slide.title}</h1>
            <div
              className="text-lg md:text-xl font-light leading-relaxed max-w-3xl space-y-4"
              dangerouslySetInnerHTML={{ __html: slide.content }}
            />
            {slide.image && (
              <img
                src={slide.image.src}
                alt={slide.image.alt}
                className={`mt-8 rounded-xl shadow-lg transition-transform duration-500 transform hover:scale-105 ${slide.image.width}`}
                style={{ maxHeight: '50vh' }}
              />
            )}
          </div>
          {/* Slide Navigation and Indicators */}
          <div className="absolute bottom-6 left-0 right-0 flex items-center justify-center space-x-4">
            <button
              onClick={prevSlide}
              disabled={currentSlide === 0}
              className={`p-3 rounded-full bg-white bg-opacity-10 text-white hover:bg-opacity-20 transition duration-300 disabled:opacity-30 disabled:cursor-not-allowed`}
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            <div className="flex space-x-2">
              {slidesData.map((_, index) => (
                <span
                  key={index}
                  className={`w-3 h-3 rounded-full transition-colors duration-300 ${
                    index === currentSlide ? 'bg-indigo-400' : 'bg-gray-500'
                  }`}
                ></span>
              ))}
            </div>
            <button
              onClick={nextSlide}
              disabled={currentSlide === slidesData.length - 1}
              className={`p-3 rounded-full bg-white bg-opacity-10 text-white hover:bg-opacity-20 transition duration-300 disabled:opacity-30 disabled:cursor-not-allowed`}
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;

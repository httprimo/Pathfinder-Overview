<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Methodology"
                    subtitle="The approach and methods used in our research"
                />

                <!-- Methodology Overview -->
                <section class="mb-16">
                    <div class="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg p-8 md:p-12 mb-8">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Methodology Overview</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Pathfinder was developed using the Rapid Application Development (RAD) model, which emphasizes rapid prototyping, continuous user involvement, and iterative refinement. RAD was selected due to the project's need for consistent validation from stakeholders such as applicants and organizations.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            This model allowed the developers to transform user requirements into working prototypes, gather real-time feedback, and revise system features dynamically. RAD is particularly effective for projects where technical and business requirements must be aligned through constant feedback, as it allows the project owner to review progress after each phase.
                        </p>
                    </div>
                </section>

                <!-- Research Phases -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Research Phases</h3>
                    <div class="space-y-8">
                        <div 
                            v-for="(phase, index) in phases" 
                            :key="index"
                            class="flex flex-col md:flex-row items-start"
                        >
                            <div class="flex-shrink-0 w-16 h-16 bg-indigo-600 text-white rounded-full flex items-center justify-center font-bold text-xl mr-6 mb-4 md:mb-0">
                                {{ index + 1 }}
                            </div>
                            <div class="flex-1 bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 transition-all duration-300">
                                <h4 class="text-xl font-semibold text-gray-900 mb-3">{{ phase.title }}</h4>
                                <p class="text-gray-600">{{ phase.description }}</p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Technologies Used -->
                <section class="bg-gray-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Technologies Used</h3>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                        <div 
                            v-for="(tech, index) in technologies" 
                            :key="index"
                            class="bg-white rounded-lg p-6 text-center border-2 border-gray-200 hover:border-indigo-500 hover:shadow-lg transition-all duration-300"
                        >
                            <div class="text-3xl mb-3">{{ tech.icon }}</div>
                            <h4 class="font-semibold text-gray-900 mb-2">{{ tech.name }}</h4>
                            <p class="text-sm text-gray-600">{{ tech.description }}</p>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import { ref } from 'vue';
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';

const phases = ref([
    {
        title: 'Requirements Planning Phase',
        description: 'The project proposal and initial concepts were presented to target administrators. Requirements were gathered through interviews with representatives from the Department of Information and Communications Technology (DICT) Region II. Administrators described their existing workflows, enabling developers to validate requirements and align system functionalities with national standards and organizational processes.'
    },
    {
        title: 'User Design Phase',
        description: 'Developers translated validated requirements into logical and visual designs. Two primary tools were utilized: Figma for creating detailed UI/UX prototypes illustrating how distinct user roles (applicants, organizations, administrators) would navigate the web application, and Lucidchart for designing the database schema to visualize entity relationships and ensure the data structure could support complex queries.'
    },
    {
        title: 'Construction Phase',
        description: 'Development transitioned to implementation using a modern web development stack: Frontend (Vue.js and Tailwind CSS), Backend (Laravel), and Database & Storage (PostgreSQL and Supabase). The development followed an iterative cycle, where modules were built, tested, and revised based on continuous feedback to ensure seamless integration of stack components.'
    },
    {
        title: 'Cutover Phase',
        description: 'The web application underwent rigorous testing and validation. The system was presented to a panel of distinct organizations (DICT Region II, Center for Digital Transformation - USLT, and TESDA Region II) to assess alignment with operational needs. All inputs and recommendations were synthesized and implemented. Following refinements, the web application was deployed online using Render to ensure live accessibility in a production environment.'
    }
]);

const technologies = ref([
    { icon: '⚛️', name: 'Vue.js', description: 'Frontend framework for building user interfaces' },
    { icon: '🎨', name: 'Tailwind CSS', description: 'Utility-first CSS framework for styling' },
    { icon: '🔧', name: 'Laravel', description: 'PHP backend framework for web applications' },
    { icon: '🗄️', name: 'PostgreSQL', description: 'Advanced open-source relational database' },
    { icon: '☁️', name: 'Supabase', description: 'Backend-as-a-Service for database and storage' },
    { icon: '🚀', name: 'Render', description: 'Cloud platform for deployment and hosting' },
    { icon: '📐', name: 'Figma', description: 'Design tool for UI/UX prototyping' },
    { icon: '📊', name: 'Lucidchart', description: 'Database schema design and visualization' }
]);
</script>


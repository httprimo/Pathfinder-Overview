<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Results"
                    subtitle="Findings, insights, and outcomes of our research"
                />

                <!-- Key Findings -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Key Findings</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div 
                            v-for="(finding, index) in findings" 
                            :key="index"
                            class="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-lg p-6 border-l-4 border-indigo-600"
                        >
                            <div class="flex items-center mb-3">
                                <div class="w-10 h-10 bg-indigo-600 text-white rounded-full flex items-center justify-center font-bold mr-3">
                                    {{ index + 1 }}
                                </div>
                                <h4 class="text-xl font-semibold text-gray-900">{{ finding.title }}</h4>
                            </div>
                            <p class="text-gray-700">{{ finding.description }}</p>
                        </div>
                    </div>
                </section>

                <!-- Results Summary -->
                <section class="mb-16">
                    <div class="bg-green-50 border-l-4 border-green-500 rounded-lg p-8 md:p-12">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Results Summary</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            The Pathfinder web application was successfully constructed using the Rapid Application Development (RAD) model, achieving stable and reliable deployment from local development to live production environment on Render. The project successfully implemented all intended software modules designed to bridge the gap between skill acquisition and employment.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Key features including the Career-Training Matching Engine, Resume Editor, and QR code-based attendance and certificate issuance system effectively digitized processes that were previously done manually. The system was validated against ISO/IEC 25010 and USE model standards, confirming that Pathfinder is a significant improvement over existing disjointed platforms.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            Ultimately, this project addresses the critical economic challenge of skills mismatch in the localized labor market of Tuguegarao City. By providing a zero-cost, centralized platform that links skills-first training opportunities directly to career paths, Pathfinder empowers vulnerable populations—specifically unemployed youth and low-income job seekers—to enhance their employability without financial barriers.
                        </p>
                    </div>
                </section>

                <!-- Insights -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Key Insights</h3>
                    <div class="space-y-6">
                        <div 
                            v-for="(insight, index) in insights" 
                            :key="index"
                            class="flex items-start bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-lg transition-all duration-300"
                        >
                            <div class="flex-shrink-0 w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mr-4">
                                <span class="text-purple-600 text-xl">💡</span>
                            </div>
                            <div class="flex-1">
                                <h4 class="text-lg font-semibold text-gray-900 mb-2">{{ insight.title }}</h4>
                                <p class="text-gray-600">{{ insight.description }}</p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Statistics or Metrics (Optional) -->
                <section class="bg-gray-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8 text-center">Research Metrics</h3>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                        <div 
                            v-for="(metric, index) in metrics" 
                            :key="index"
                            class="bg-white rounded-lg p-6 text-center border-2 border-gray-200 hover:border-indigo-500 transition-all duration-300"
                        >
                            <div class="text-4xl font-bold text-indigo-600 mb-2">{{ metric.value }}</div>
                            <div class="text-gray-600 text-sm">{{ metric.label }}</div>
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

const findings = ref([
    {
        title: 'High End-User Satisfaction',
        description: 'The web application achieved an overall mean rating of 4.55 (Strongly Agree) from 34 end-users, with "Ease of Use" receiving the highest individual score of 4.64. This indicates that the interface design was highly intuitive for college students and job seekers.'
    },
    {
        title: 'Strong Technical Quality',
        description: 'Evaluation by 13 IT experts yielded an overall mean of 4.07 (Agree) based on ISO/IEC 25010 standards, with "Portability" scoring highest at 4.15, confirming the system\'s adaptability across different operational environments.'
    },
    {
        title: 'Excellent Usability Metrics',
        description: 'All USE Questionnaire criteria received "Strongly Agree" ratings: Usefulness (4.63), Ease of Use (4.64), Ease of Learning (4.51), and Satisfaction (4.43). Users could quickly master the web application functionalities without extensive instruction.'
    },
    {
        title: 'Comprehensive Quality Standards',
        description: 'All ISO/IEC 25010 characteristics received "Agree" ratings: Functional Suitability (4.03), Compatibility (4.08), Usability (4.08), Security (4.00), and Portability (4.15), confirming the system successfully met its objectives.'
    }
]);

const insights = ref([
    {
        title: 'User-Centric Design Success',
        description: 'The high "Ease of Use" rating (4.64) demonstrates that the interface design, specifically the navigation flows for searching careers and trainings, was intuitive for the target audience. This validates the effectiveness of the RAD methodology\'s emphasis on continuous user involvement and iterative refinement.'
    },
    {
        title: 'Centralized Platform Value',
        description: 'The "Usefulness" rating of 4.63 confirms that respondents found the web application\'s core purpose of centralizing training and career opportunities highly relevant to their needs. This addresses the critical gap in existing platforms that require users to navigate multiple websites.'
    },
    {
        title: 'Technical Adaptability',
        description: 'The highest-rated ISO 25010 characteristic was "Portability" (4.15), indicating that experts found the web application adaptable across different environments and devices. This confirms the system\'s readiness for broader deployment beyond Tuguegarao City.'
    },
    {
        title: 'Skills-Based Approach Validation',
        description: 'The positive evaluation results validate Pathfinder\'s approach to skills-based hiring. The system successfully provides a centralized, secure, and compatible platform that effectively replaces the need to navigate multiple websites for training and job applications, addressing the skills mismatch challenge.'
    }
]);

const metrics = ref([
    { value: '4.55', label: 'Overall End-User Rating (Strongly Agree)' },
    { value: '4.64', label: 'Ease of Use Score (Highest)' },
    { value: '34', label: 'End-User Evaluators' },
    { value: '13', label: 'IT Expert Evaluators' },
    { value: '4.07', label: 'Overall Expert Rating (Agree)' },
    { value: '4.15', label: 'Portability Score (Highest)' }
]);
</script>


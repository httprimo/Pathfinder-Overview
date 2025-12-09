<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="System Features"
                    subtitle="Key features and capabilities of our research system"
                />

                <!-- Features Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
                    <div 
                        v-for="(feature, index) in features" 
                        :key="index"
                        class="bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
                    >
                        <div class="text-4xl mb-4">{{ feature.icon }}</div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-3">{{ feature.title }}</h3>
                        <p class="text-gray-600">{{ feature.description }}</p>
                    </div>
                </div>

                <!-- System Screenshots Carousel -->
                <section class="mb-16 -mx-4 sm:-mx-6 lg:-mx-8">
                    <div class="w-full bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-50 py-8">
                        <!-- Header with Page Indicator and Navigation -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-4">
                                    <div class="bg-customButton text-white px-4 py-2 rounded-full font-semibold text-sm">
                                        {{ currentStepData?.description || 'System screenshot' }}
                                    </div>
                                </div>
                                <div class="flex items-center gap-2">
                                    <button
                                        @click="previousScreenshotStep"
                                        :disabled="currentScreenshotStep === 0"
                                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                                    >
                                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                                        </svg>
                                    </button>
                                    <button
                                        @click="nextScreenshotStep"
                                        :disabled="currentScreenshotStep === screenshotSteps.length - 1"
                                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                                    >
                                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Main Content Area -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
                                <!-- Left Panel - Screenshot Display -->
                                <div class="bg-gradient-to-br from-purple-100 to-indigo-100 rounded-2xl p-8 shadow-xl">
                                    <div class="bg-white rounded-lg overflow-hidden shadow-lg group">
                                        <img
                                            :src="currentStepData?.image"
                                            :alt="currentStepData?.description || `Step ${currentScreenshotStep + 1}`"
                                            class="w-full h-auto transition-transform duration-300 ease-in-out group-hover:scale-105"
                                            @error="handleScreenshotError"
                                        />
                                    </div>
                                </div>

                                <!-- Right Panel - Description -->
                                <div class="space-y-4">
                                    <h2 class="text-4xl font-bold text-customButton mb-4">
                                        {{ currentStepData?.description || 'System screenshot showing key functionality.' }}
                                    </h2>
                                    <div v-if="currentStepData?.details && currentStepData.details.length > 0" class="mt-6 space-y-2">
                                        <h3 class="text-xl font-semibold text-gray-800">Key Features:</h3>
                                        <ul class="list-disc list-inside space-y-1 text-gray-600">
                                            <li v-for="(detail, index) in currentStepData.details" :key="index">{{ detail }}</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Pagination Dots and Progress Bar -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
                            <!-- Pagination Dots -->
                            <div class="flex justify-center items-center gap-3 mb-4 flex-wrap">
                                <button
                                    v-for="(step, index) in screenshotSteps"
                                    :key="index"
                                    @click="goToScreenshotStep(index)"
                                    class="w-10 h-10 rounded-full border-2 flex items-center justify-center font-semibold text-sm transition-all"
                                    :class="index === currentScreenshotStep 
                                        ? 'bg-customButton text-white border-customButton' 
                                        : 'bg-white text-gray-700 border-gray-300 hover:border-customButton hover:bg-purple-50'"
                                >
                                    {{ index + 1 }}
                                </button>
                            </div>

                            <!-- Progress Bar -->
                            <div class="w-full max-w-4xl mx-auto">
                                <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                                    <div
                                        class="h-full bg-customButton transition-all duration-300 ease-out"
                                        :style="{ width: `${((currentScreenshotStep + 1) / screenshotSteps.length) * 100}%` }"
                                    ></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>


                <!-- Additional Features List -->
                <section class="bg-indigo-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Additional Features</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div 
                            v-for="(item, index) in additionalFeatures" 
                            :key="index"
                            class="flex items-center"
                        >
                            <svg class="w-6 h-6 text-indigo-600 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                            </svg>
                            <span class="text-gray-700">{{ item }}</span>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';

const features = ref([
    {
        icon: '🎯',
        title: 'Career-Training Matching Engine',
        description: 'Automatically matches the target career selected by applicants with training posts that have similar tags, helping users find relevant skill development opportunities aligned with their career goals.'
    },
    {
        icon: '📝',
        title: 'Resume Editor',
        description: 'Streamlines document preparation by allowing applicants to generate professional resumes with fields for professional summary, experience, education, and skills. Includes certificate management integration.'
    },
    {
        icon: '📅',
        title: 'Calendar & Event Management',
        description: 'Displays scheduled training events and interview dates. Applicants can view their registered trainings and applied careers, while organizations can manage their event schedules efficiently.'
    },
    {
        icon: '🔍',
        title: 'Advanced Search & Filtering',
        description: 'Multi-filter search functionality allowing users to search for careers, trainings, and organizations. The search bar contains three filters: career, training, and organization for precise results.'
    },
    {
        icon: '✅',
        title: 'QR Code Attendance System',
        description: 'QR code-based attendance and certificate issuance system that digitizes processes previously done manually. Organizations can generate QR codes for training sessions and issue certificates to eligible participants.'
    },
    {
        icon: '👥',
        title: 'Organization Verification',
        description: 'Administrative workflow for verifying organization accounts. Organizations must submit required documents for verification before they can post trainings and career opportunities, ensuring platform credibility.'
    },
    {
        icon: '📊',
        title: 'Dashboard Analytics',
        description: 'Organization dashboard displays statistics for career and training posts, providing insights into registrations, applications, and overall engagement metrics.'
    },
    {
        icon: '📄',
        title: 'Document Management',
        description: 'Applicants can upload and manage certificates obtained outside the system, and include them in their resume. The system also tracks certificates issued by organizations for trainings attended within the platform.'
    },
    {
        icon: '💼',
        title: 'Application Tracking',
        description: 'Applicants can track the status of their career applications (submitted, for review, for interview, hired/declined) and training registrations (upcoming, ongoing, conducted).'
    }
]);

const additionalFeatures = ref([
    'User Registration & Authentication (Applicants, Organizations, Admin)',
    'Email Verification System',
    'Profile Management & Account Settings',
    'Training Post Creation & Management',
    'Career Opportunity Posting & Management',
    'Interview Scheduling System',
    'Certificate Generation & Issuance',
    'Activity Tracking & History',
    'Multi-role Access Control',
    'Responsive Web Design',
    'Real-time Status Updates',
    'Secure File Upload & Storage'
]);

// System Screenshots Steps - All 27 pages from the User Manual PDF
const screenshotSteps = ref([
    {
        description: 'User Manual - Introduction and overview of the PATHFINDER system.',
        image: '/images/screenshots/page-01.png'
    },
    {
        description: 'System features and key functionalities.',
        image: '/images/screenshots/page-02.png'
    },
    {
        description: 'User interface and navigation guide.',
        image: '/images/screenshots/page-03.png'
    },
    {
        description: 'Registration and account creation process.',
        image: '/images/screenshots/page-04.png'
    },
    {
        description: 'Login and authentication procedures.',
        image: '/images/screenshots/page-05.png'
    },
    {
        description: 'Dashboard overview and main features.',
        image: '/images/screenshots/page-06.png'
    },
    {
        description: 'Profile management and settings.',
        image: '/images/screenshots/page-07.png'
    },
    {
        description: 'Career search and browsing functionality.',
        image: '/images/screenshots/page-08.png'
    },
    {
        description: 'Training search and filtering options.',
        image: '/images/screenshots/page-09.png'
    },
    {
        description: 'Resume builder and editor features.',
        image: '/images/screenshots/page-10.png'
    },
    {
        description: 'Application tracking and status monitoring.',
        image: '/images/screenshots/page-11.png'
    },
    {
        description: 'Calendar view and event management.',
        image: '/images/screenshots/page-12.png'
    },
    {
        description: 'Certificate management and upload.',
        image: '/images/screenshots/page-13.png'
    },
    {
        description: 'Organization dashboard and analytics.',
        image: '/images/screenshots/page-14.png'
    },
    {
        description: 'Training post creation and management.',
        image: '/images/screenshots/page-15.png'
    },
    {
        description: 'Career posting and management tools.',
        image: '/images/screenshots/page-16.png'
    },
    {
        description: 'QR code attendance system.',
        image: '/images/screenshots/page-17.png'
    },
    {
        description: 'Certificate generation and issuance.',
        image: '/images/screenshots/page-18.png'
    },
    {
        description: 'Interview scheduling and management.',
        image: '/images/screenshots/page-19.png'
    },
    {
        description: 'Search and filtering functionality.',
        image: '/images/screenshots/page-20.png'
    },
    {
        description: 'Tag-based matching system.',
        image: '/images/screenshots/page-21.png'
    },
    {
        description: 'Organization verification process.',
        image: '/images/screenshots/page-22.png'
    },
    {
        description: 'Admin panel and user management.',
        image: '/images/screenshots/page-23.png'
    },
    {
        description: 'System settings and configuration.',
        image: '/images/screenshots/page-24.png'
    },
    {
        description: 'Notifications and messaging system.',
        image: '/images/screenshots/page-25.png'
    },
    {
        description: 'Help and support documentation.',
        image: '/images/screenshots/page-26.png'
    },
    {
        description: 'Appendix and additional resources.',
        image: '/images/screenshots/page-27.png'
    }
]);

// Carousel state
const currentScreenshotStep = ref(0);

// Computed property for current step data
const currentStepData = computed(() => {
    return screenshotSteps.value[currentScreenshotStep.value] || null;
});

// Navigation functions
const nextScreenshotStep = () => {
    if (currentScreenshotStep.value < screenshotSteps.value.length - 1) {
        currentScreenshotStep.value++;
    }
};

const previousScreenshotStep = () => {
    if (currentScreenshotStep.value > 0) {
        currentScreenshotStep.value--;
    }
};

const goToScreenshotStep = (index) => {
    if (index >= 0 && index < screenshotSteps.value.length) {
        currentScreenshotStep.value = index;
    }
};

const handleScreenshotError = (event) => {
    event.target.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="800" height="600"%3E%3Crect fill="%23f3f4f6" width="800" height="600"/%3E%3Ctext x="50%25" y="50%25" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="24" fill="%239ca3af"%3EScreenshot not found%3C/text%3E%3C/svg%3E';
};


// Keyboard navigation
let keyboardHandler = null;

onMounted(() => {
    keyboardHandler = (e) => {
        if (e.key === 'ArrowLeft') {
            previousScreenshotStep();
        } else if (e.key === 'ArrowRight') {
            nextScreenshotStep();
        }
    };
    window.addEventListener('keydown', keyboardHandler);
});

onUnmounted(() => {
    if (keyboardHandler) {
        window.removeEventListener('keydown', keyboardHandler);
    }
});
</script>


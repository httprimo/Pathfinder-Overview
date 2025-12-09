<?php

namespace App\Http\Controllers;

use Inertia\Inertia;

class ResearchController extends Controller
{
    public function home()
    {
        return Inertia::render('Research/Home');
    }

    public function about()
    {
        return Inertia::render('Research/About');
    }

    public function objectives()
    {
        return Inertia::render('Research/Objectives');
    }

    public function features()
    {
        return Inertia::render('Research/Features');
    }

    public function methodology()
    {
        return Inertia::render('Research/Methodology');
    }

    public function architecture()
    {
        return Inertia::render('Research/Architecture');
    }

    public function results()
    {
        return Inertia::render('Research/Results');
    }

    public function team()
    {
        return Inertia::render('Research/Team');
    }
}


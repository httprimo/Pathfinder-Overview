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

    public function features()
    {
        return Inertia::render('Research/Features');
    }

    public function team()
    {
        return Inertia::render('Research/Team');
    }
}


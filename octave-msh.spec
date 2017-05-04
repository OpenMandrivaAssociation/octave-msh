%define octpkg msh

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Meshes for finite element/volume PDE Octave solvers
Name:		octave-%{octpkg}
Version:	1.0.10
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-splines

Requires(post): octave
Requires(postun): octave

%description
Create and manage triangular and tetrahedral meshes for Finite Element or
Finite Volume PDE solvers in Octave. Use a mesh data structure compatible
with PDEtool. Rely on gmsh for unstructured mesh generation.

This package is part of external Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING


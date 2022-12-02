%define octpkg msh

Summary:	Meshes for finite element/volume PDE Octave solvers
Name:		octave-%{octpkg}
Version:	1.0.10
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?51970
Patch0:		continuation-lines.patch
# https://savannah.gnu.org/bugs/index.php?59613
Patch1:		build-against-octave-6.patch
# https://savannah.gnu.org/bugs/?41724
Patch2:		configure-script-source.patch

License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/

BuildRequires:	octave-devel >= 3.0
BuildRequires:	octave-splines
BuildRequires:	pkgconfig(dolfin)
# unpackaged
#BuildRequires:	pkgconfig(gmsh)

Requires:	octave(api) = %{octave_api}
Requires:	octave-splines
Requires:	awk

Requires(post): octave
Requires(postun): octave

%description
Create and manage triangular and tetrahedral meshes for Finite Element or
Finite Volume PDE solvers in Octave. Use a mesh data structure compatible
with PDEtool. Rely on gmsh for unstructured mesh generation.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild


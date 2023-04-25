%global octpkg msh

%bcond_with	dolfin

%if %{without dolfin}
%global debug_package %{nil}
%endif

Summary:	Meshes for finite element/volume PDE Octave solvers
Name:		octave-msh
Version:	1.0.12
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/msh/
Url:		https://github.com/carlodefalco/msh
Source0:	https://github.com/carlodefalco/msh/archive/v%{version}/msh-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?51970
Patch0:		continuation-lines.patch

BuildRequires:  octave-devel >= 3.0.0
BuildRequires:  octave-splines
%if %{with dolfin}
BuildRequires:	pkgconfig(dolfin)
%endif

Requires:	octave(api) = %{octave_api}
Requires:  	octave-splines
# unpackaged
#Requires:	gmsh

Requires(post): octave
Requires(postun): octave

%description
Create and manage triangular and tetrahedral meshes for Finite
Element or Finite Volume PDE solvers. Use a mesh data structure
compatible with PDEtool. Rely on gmsh for unstructured mesh
generation.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%if %{with dolfin}
%dir %{octpkglibdir}
%{octpkglibdir}/*
%endif

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%if %{with dolfin}
mv cruft/src .
pushd src
autoreconf -fiv 
popd
%endif
rm -fr cruft

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


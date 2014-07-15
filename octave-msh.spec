%define	pkgname msh

Summary:	Meshes for finite element/volume PDE Octave solvers
Name:       octave-%{pkgname}
Version:	1.0.2
Release:        4
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/msh/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.0.0, octave-splines >= 0.0.0
BuildRequires:  octave-devel >= 3.0.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildArch:	noarch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Create and manage triangular and tetrahedral meshes for finite element
or finite volume PDE solvers in Octave. Use a mesh data structure
compatible with PDEtool. Rely on gmsh for unstructured mesh
generation.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0} 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}

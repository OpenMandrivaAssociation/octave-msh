%define	pkgname msh
%define name	octave-%{pkgname}
%define version 1.0.2

Summary:	Meshes for finite element/volume PDE Octave solvers
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/msh/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.0.0, octave-splines >= 0.0.0
BuildRequires:  octave-devel >= 3.0.0
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildArch:	noarch

%description
Create and manage triangular and tetrahedral meshes for finite element
or finite volume PDE solvers in Octave. Use a mesh data structure
compatible with PDEtool. Rely on gmsh for unstructured mesh
generation.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}



%changelog
* Mon Aug 22 2011 Lev Givon <lev@mandriva.org> 1.0.2-1mdv2012.0
+ Revision: 696175
- import octave-msh



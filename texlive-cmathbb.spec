%global tl_name cmathbb
%global tl_revision 56414

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Computer modern mathematical blackboard bold font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cmathbb
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmathbb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmathbb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This font contains all digits and latin letters uppercase and lowercase
for the Computer Modern font family in blackboard bold.


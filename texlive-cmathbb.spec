%global tl_name cmathbb
%global tl_revision 56414
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Computer modern mathematical blackboard bold font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cmathbb
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmathbb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmathbb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This font contains all digits and latin letters uppercase and lowercase
for the Computer Modern font family in blackboard bold.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from cmathbb:
Map cmathbb.map
TL_DROPIN_EOF

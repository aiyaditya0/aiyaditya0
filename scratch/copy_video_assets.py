import os
import shutil

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    src_dir = os.path.join(root_dir, "500 gb editing Pack", "500 GB editing Pack")
    dest_dir = os.path.join(root_dir, "video-editing-assets")
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")
        
    if not os.path.exists(src_dir):
        print(f"Error: Source directory {src_dir} does not exist!")
        return

    # List of files we want to copy (showcase bundles and the hero image)
    files_to_copy = [
        "bundle-ae-plugins-CyVLB4fl.webp",
        "bundle-animated-title-CYf6cNVp.webp",
        "bundle-backgrounds-Oh9fMsFW.webp",
        "bundle-callout-DuFRIPMy.webp",
        "bundle-cinematic-luts-BaGIucCs.webp",
        "bundle-dust-snow-B-4aPUme.webp",
        "bundle-emoji-ycOYV4KV.webp",
        "bundle-film-grain-Y98RWxcZ.webp",
        "bundle-fire-spark-C_teSlsk.webp",
        "bundle-fonts-Bu_TFDEz.webp",
        "bundle-fx-presets-D38CBVQK.webp",
        "bundle-glitch-effects-DzFEWAhy.webp",
        "bundle-lens-bokeh-C1EQj8aH.webp",
        "bundle-light-leak-CwWR9BR4.webp",
        "bundle-logo-animation-DtVPv01w.webp",
        "bundle-lower-third-2-CTliT4Xz.webp",
        "bundle-motion-graphic-CVy_4PUE.webp",
        "bundle-rain-BHbktu0V.webp",
        "bundle-royalty-music-DVY_BmKF.webp",
        "bundle-smoke-HlE8uUXG.webp",
        "bundle-sound-effects-p1Mqffr0.webp",
        "bundle-stock-videos-DhN_uQ4X.webp",
        "bundle-transitions-Dtk8-IJp.webp",
        "bundle-video-course-susGdk4p.webp",
        "bundle-wedding-invitation-2-3Q-muq3v.webp",
        "bundle-wedding-invitation-kSZ58WIb.webp",
        "bundle-youtube-CWYca0Js.webp",
        "hero-toolkit-zkCHdDKW.webp"
    ]

    copied_count = 0
    for filename in files_to_copy:
        src_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"Copied: {filename}")
            copied_count += 1
        else:
            print(f"Warning: File {filename} not found in source!")

    print(f"\nDone! Copied {copied_count} files to {dest_dir}")

if __name__ == "__main__":
    main()

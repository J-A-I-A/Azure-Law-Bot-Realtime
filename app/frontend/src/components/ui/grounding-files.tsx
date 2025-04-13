import { AnimatePresence, motion, Variants } from "framer-motion";
import { useState } from "react";
import { ChevronDown, ChevronUp, File } from "lucide-react";

import { GroundingFile as GroundingFileType } from "@/types";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./card";
import { Button } from "./button";
import GroundingFile from "./grounding-file";
import { useRef } from "react";
import { useTranslation } from "react-i18next";

type Properties = {
    files: GroundingFileType[];
    onSelected: (file: GroundingFileType) => void;
};

const variants: Variants = {
    hidden: { opacity: 0, scale: 0.8, y: 20 },
    visible: (i: number) => ({
        opacity: 1,
        scale: 1,
        y: 0,
        transition: {
            delay: i * 0.1,
            duration: 0.3,
            type: "spring",
            stiffness: 300,
            damping: 20
        }
    })
};

export function GroundingFiles({ files, onSelected }: Properties) {
    const { t } = useTranslation();
    const isAnimating = useRef(false);
    const [isExpanded, setIsExpanded] = useState(true);

    if (files.length === 0) {
        return null;
    }

    return (
        <Card className="m-4 max-w-full md:max-w-md lg:min-w-96 lg:max-w-2xl">
            <CardHeader className="pb-2 flex flex-row items-center justify-between">
                <div>
                    <CardTitle className="text-xl">{t("groundingFiles.title")}</CardTitle>
                    <CardDescription>{t("groundingFiles.description")}</CardDescription>
                </div>
                <Button 
                    variant="ghost" 
                    size="sm"
                    className="rounded-full h-8 w-8 p-0"
                    onClick={() => setIsExpanded(!isExpanded)}
                    aria-label={isExpanded ? t("groundingFiles.collapse") : t("groundingFiles.expand")}
                    title={isExpanded ? t("groundingFiles.collapse") : t("groundingFiles.expand")}
                >
                    {isExpanded ? <ChevronUp className="h-5 w-5" /> : <ChevronDown className="h-5 w-5" />}
                </Button>
            </CardHeader>
            <AnimatePresence initial={false}>
                {isExpanded && (
                    <motion.div
                        key="content"
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.3 }}
                    >
                        <CardContent>
                            <AnimatePresence>
                                <motion.div
                                    initial={{ opacity: 0 }}
                                    animate={{ opacity: 1 }}
                                    exit={{ opacity: 0 }}
                                    transition={{ duration: 0.3 }}
                                    className={`h-full ${isAnimating ? "overflow-hidden" : "overflow-y-auto"}`}
                                    onLayoutAnimationStart={() => (isAnimating.current = true)}
                                    onLayoutAnimationComplete={() => (isAnimating.current = false)}
                                >
                                    <div className="flex flex-wrap gap-2">
                                        {files.map((file, index) => (
                                            <motion.div key={index} variants={variants} initial="hidden" animate="visible" custom={index}>
                                                <GroundingFile key={index} value={file} onClick={() => onSelected(file)} />
                                            </motion.div>
                                        ))}
                                    </div>
                                </motion.div>
                            </AnimatePresence>
                        </CardContent>
                    </motion.div>
                )}
            </AnimatePresence>
        </Card>
    );
}

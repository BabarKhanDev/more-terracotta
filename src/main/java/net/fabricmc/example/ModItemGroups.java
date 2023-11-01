package net.fabricmc.example;

import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.block.Blocks;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

public class ModItemGroups {

    // Register Our Item Groups
    public static final ItemGroup TERRACOTTA_GROUP = FabricItemGroup.builder(Identifier.of("moreterracotta", "terracotta_group"))
            .displayName(Text.translatable("More Terracotta"))
            .icon(() -> new ItemStack(Blocks.TERRACOTTA))
            .build();

    public static final ItemGroup CONCRETE_GROUP = FabricItemGroup.builder(Identifier.of("moreterracotta", "concrete_group"))
            .displayName(Text.translatable("More Concrete"))
            .icon(() -> new ItemStack(Blocks.WHITE_CONCRETE))
            .build();

}
